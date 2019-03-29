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
t = open("TwitterSecret.txt", "r")
c = open("ConsumerSecret.txt", "r")
access_token = "3303963448-DYXKxwkKTeOZPScOBgXVGLDfrl8DR0ZQsrQvMQp"
access_token_secret =  t.read()
consumer_key = "anEmKfK4WLIW5IIPyQk7mgWLn"
consumer_secret = c.read()

api = twitter.Api(consumer_key,consumer_secret,access_token,access_token_secret, tweet_mode='extended')


f = open("TOKEN.txt", "r")
TOKEN = f.read();

client = discord.Client()

@client.event
async def on_message(message):
    rand = random.randint(0,200)
    text = message.content.lower()
    #Add Emoji Reaction to any message containing 'bork'
    if "bork" in text:
        emojRi = get(client.get_all_emojis(), name="\U0001F415")
        await client.add_reaction(message, "\U0001F415")



    #if message author is bot
    if message.author == client.user:
        #Add emoji reaction to any message sent by the bot
        emoji = get(client.get_all_emojis(), name="\U0001F436")
        await client.add_reaction(message, "\U0001F436")
        #stop the bot replying to itself
        return

    #get 20 latest tweets from @dog_feelings and add them to a dict
    t = api.GetUserTimeline(screen_name="dog_feelings", count=20)
    tweets = [i.AsDict() for i in t]

    #if message starts with 'hello doggo', say hello and @ the person who said it
    if text.startswith('hello doggo'):
        msg = 'Henlo {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    #if message starts with 'what are you thinking doggo?'
    if text.startswith('what are you thinking doggo?'):
        #get random tweet from the dict of tweets
        msg = tweets[random.randint(0,20)]['full_text']
        #send tweet as message
        await client.send_message(message.channel, msg)

    #if message starts with 'doggo show me a doggo' send a pic of a doggo from folder
    if text.startswith('doggo show me a doggo'):
        list = os.listdir(dir_path+'/Doggos')
        number_files = len(list)
        #get random number for image
        rando = random.randint(1,number_files)
        with open(dir_path+'/Doggos/'+str(rando)+'.jpg', 'rb') as picture:
            await client.send_file(message.channel,picture)

    #if message contains 'good boy' or 'good boi' reply with 'im a good boy'
    if "good boy" in message.content or "good boi" in message.content:
        await client.send_message(message.channel, 'im a good boy')

    #if message contains 'woof' reply with 'bork' and vice versa
    if "woof" in text:
        await client.send_message(message.channel, 'bork')

    if "cat" in text:
        await client.send_message(message.channel, 'WOOF! BORK! WOOF!')

    if "bork" in text:
        await client.send_message(message.channel, 'woof')

    #at random send a message of 'woof woof' or 'bork bork'
    if rand == 50:
        await client.send_message(message.channel, 'woof woof')

    if rand == 20:
        await client.send_message(message.channel, 'bork bork')


@client.event
#log basic info when the bot starts running
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)