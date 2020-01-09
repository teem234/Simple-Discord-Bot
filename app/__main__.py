import discord
import asyncio


from app.MusicManager import MusicManager
from app import client
from app import myCode

#tokenz = secretcode.myCode
#client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('-test'):
        #msg = 'Hello {0.author.mention} bot structure better organized now maybe. Need to move bot token to private file retard'.format(message)
        msg = ':crab: :crab: Hi im a bot' :crab: :crab:'
        await message.channel.send(msg.format(message.author))

    if message.content.startswith('-test2'):
        #msg = 'Hello {0.author.mention} bot structure better organized now maybe. Need to move bot token to private file retard'.format(message)
        msg = 'still here'
        await message.channel.send(msg.format(message.author))
    if message.content.startswith('-play'):
        botInst = MusicManager('me')

        msg = 'Playing song'.format(message)
        await botInst.test(message)
        #await message.channel.send(msg.format(message.author))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(myCode)
