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
from os import walk
from discord.utils import get
dir_path = os.path.dirname(os.path.realpath(__file__))

#Variables that contains the user credentials to access Twitter API
t = open("TwitterSecret.txt", "r")
c = open("ConsumerSecret.txt", "r")
access_token = "3303963448-DYXKxwkKTeOZPScOBgXVGLDfrl8DR0ZQsrQvMQp"
access_token_secret =  t.read()
consumer_key = "anEmKfK4WLIW5IIPyQk7mgWLn"
consumer_secret = c.read()
pic_ext = ['.jpg','.png','.jpeg']

api = twitter.Api(consumer_key,consumer_secret,access_token,access_token_secret, tweet_mode='extended')
rate = ["Excellent Woofer", "Much Cute", "Lovely Doggo", "Thats a big ol' pupper"]

f = open("TOKEN.txt", "r")
TOKEN = f.read();

client = discord.Client()

@client.event
async def on_message(message):
    rand = random.randint(0,200)
    text = message.content.lower()

    #Add Emoji Reaction to any message containing 'bork'
    if "bork" in text:
        await client.add_reaction(message, "\U0001F415")

    #if message author is this bot
    if message.author == client.user:
        #Add emoji reaction to any message sent by the bot
        emoji = get(client.get_all_emojis(), name="\U0001F436")
        await client.add_reaction(message, "\U0001F436")
        #stop the bot replying to itself
        return

    #if author is any bot
    if message.author.bot == True:
        #stop bot from responding
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
        #get list of files
        l = os.listdir(dir_path+'/Doggos')
        number_files = len(l)
        #get random number for image
        rando = random.randint(1,number_files)
        #send the file
        with open(dir_path+'/Doggos/'+l[rando-1], 'rb') as picture:
            m = await client.send_file(message.channel,picture)
        await client.add_reaction(m, "❤")

    if "test" in text:
        embed = discord.Embed();
        embed.set_thumbnail(url='https://images.dog.ceo/breeds/chow/n02112137_5089.jpg')
        await client.send_message(message.channel, embed=embed)

    #if some asks 'doggo rate my doggo' and they have a file
    if text.startswith('doggo rate my doggo') and "filename" in message.attachments[0]:
        for i in pic_ext:
            #if attached file is an image
            if (message.attachments[0]["filename"]).endswith(i):
                #react with a heart to the image they sent
                await client.add_reaction(message, "❤")
                #get random numbers for rating and message responce
                choice = random.randint(0,len(rate))
                rating = random.randint(10,21)
                #reply with at least 10/10 and a random message from list
                msg = str(rating) + "/10 " + rate[choice]
                await client.send_message(message.channel,msg)

    #if message contains 'good boy' or 'good boi'
    if "good boy" in text or "good boi" in text:
        #reply with 'im a good boy'
        await client.send_message(message.channel, 'im a good boy')

    #if message contains 'woof'
    if "woof" in text:
        #reply with 'bork' and vice versa
        await client.send_message(message.channel, 'bork')

    if "bork" in text:
        await client.send_message(message.channel, 'woof')

    #if message contains 'cat'
    if "cat" in text:
        #reply with 'WOOF! BORK WOOF!'
        await client.send_message(message.channel, 'WOOF! BORK! WOOF!')

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