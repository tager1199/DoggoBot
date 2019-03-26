#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Thomas
#
# Created:     26/03/2019
# Copyright:   (c) Thomas 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import discord
import twitter
import random
import os
from discord.utils import get
dir_path = os.path.dirname(os.path.realpath(__file__))

#Variables that contains the user credentials to access Twitter API
access_token = "3303963448-DYXKxwkKTeOZPScOBgXVGLDfrl8DR0ZQsrQvMQp"
access_token_secret = "M344sq15rUGchM6h03zx2DqeKmiJzhAPLLnyp3YCagFnA"
consumer_key = "anEmKfK4WLIW5IIPyQk7mgWLn"
consumer_secret = "lxReKcp7LsXEpPOETRSVGttHfQE4RHkr4WIcXVlj2zOD7AJoAL"

api = twitter.Api(consumer_key,consumer_secret,access_token,access_token_secret, tweet_mode='extended')



TOKEN = 'NDA2MDEwNDkwMzMwOTM5Mzky.D3rNdQ.JS5uvJ-9KnACUyHUw8OBEDkPvV0'

client = discord.Client()

@client.event
async def on_message(message):
    rand = random.randint(0,1000)
    #we do not want the bot to reply to itself

    if "bork" in message.content:
        emoji = get(bot.get_all_emojis(), name='doge')
        await bot.add_reaction(message, emoji)




    if message.author == client.user:
        return

    if message.content.startswith('hello doggo'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('what are you thinking doggo?'):
        t = api.GetUserTimeline(screen_name="dog_feelings", count=20)
        tweets = [i.AsDict() for i in t]
        msg = tweets[random.randint(0,20)]['full_text']
        await client.send_message(message.channel, msg)

    if message.content.startswith('doggo show me a doggo'):
        rando = random.randint(0,35) + 1
        with open(dir_path+'/Doggos/'+str(rando)+'.jpg', 'rb') as picture:
            await client.send_file(message.channel,picture)

    if "good boy" in message.content:
        await client.send_message(message.channel, 'im a good boy')

    if "good boi" in message.content:
        await client.send_message(message.channel, 'im a good boy')

    if "woof" in message.content:
        await client.send_message(message.channel, 'bork')


    if "bork" in message.content:
        await client.send_message(message.channel, 'woof')

    if rand == 500:
        await client.send_message(message.channel, 'woof woof')

    if rand == 200:
        await client.send_message(message.channel, 'bork bork')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)