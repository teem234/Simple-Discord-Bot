Created by Timothy Joyce

python 3.7.1

#Some requirements:
youtube-dl
pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip#egg=discord.py[voice]
asyncio
must pip install ffmpeg and download binary and make path set

#Description
A simple bot created for use on the voice messaging software Discord.
Current functionality includes responding to user commands and playing music.


On discord, if a user types "-play <youtubelink>" while in a voice channel, the bot will join the
user's voice channel and play the song from youtube. There is no video only audio.
Audio may disconnect due to issue with discord.py library used. Workaround will be found. Many other
discord python bots use Python2 instead to avoid previous issue.
