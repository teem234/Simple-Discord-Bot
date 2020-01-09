from __future__ import unicode_literals
import youtube_dl
import discord
import ffmpeg
from app import client

youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

    
class MusicManager:
    def __init__(self,user):
        self.usesr = user
        self.bot = client
        
    async def test(self,message):
        result=''
        print('executing music code')
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }],
            'outtmpl': '%(title)s.%(etx)s',
            'quiet': False
        }
	#predefined url for now
        url = 'https://www.youtube.com/watch?v=1vrEljMfXYo'
        #setx /M PATH "E:\Documents\discbot\discbot\libs\ffmpeg-20190129-2e2b44b-win64-static;%PATH%"
        user = message.author
        voice_channel = user.voice.channel
        
        #vc = await client.join_voice_channel(voice_channel)
        #message.state.voice = await voice_channel.connect()
        try: 
            vc = await voice_channel.connect()
        except discord.ClientException:
            await message.channel.send('Already in a voice channel'.format(message.author))
            
        #player = await vc.create_ytdl_player(url)
        #player = vc.play(discord.FFmpegPCMAudio(url))

        player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
        vc.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
        
        #player.start()
        
        
        """ 
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # cwd
            result = ydl.extract_info(
                url,
                download=False
            )
        print(result)
        """
        

  
    

