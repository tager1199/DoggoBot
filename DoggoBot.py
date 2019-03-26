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
    #we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('hello doggo'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        #send_file(destination, fp, *, filename=None, content=None, tts=False)


    if message.content.startswith('what are you thinking doggo?'):
        t = api.GetUserTimeline(screen_name="dog_feelings", count=20)
        tweets = [i.AsDict() for i in t]
        msg = tweets[random.randint(0,20)]['full_text']
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)