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
import urllib.request
import json
import os
from os import walk
from discord.utils import get
dir_path = os.path.dirname(os.path.realpath(__file__))

#Variables that contains the user credentials to access Twitter API
t = open("/home/pi/Desktop/DoggoBot/TwitterSecret.txt", "r")
c = open("/home/pi/Desktop/DoggoBot/ConsumerSecret.txt", "r")
access_token = "3303963448-DYXKxwkKTeOZPScOBgXVGLDfrl8DR0ZQsrQvMQp"
access_token_secret =  t.read()
consumer_key = "anEmKfK4WLIW5IIPyQk7mgWLn"
consumer_secret = c.read()
pic_ext = ['.jpg','.png','.jpeg']
api = twitter.Api(consumer_key,consumer_secret,access_token,access_token_secret, tweet_mode='extended')
rate = ["Excellent Woofer", "Much Cute", "Lovely Doggo", "Thats a big ol' pupper"]

f = open("/home/pi/Desktop/DoggoBot/TOKEN.txt", "r")
TOKEN = f.read();

client = discord.Client()

@client.event
async def on_message(message):
    rand = random.randint(0,200)
    text = message.content.lower()
    msg = ""
    author = message.author
    channel = message.channel
    #Add Emoji Reaction to any message containing 'bork'
    if "bork" in text:
        await message.add_reaction("\U0001F415")

    #if message author is this bot
    if author == client.user:
        #Add emoji reaction to any message sent by the bot
        await message.add_reaction("\U0001F436")
        #stop the bot replying to itself
        return

    #if author is any bot
    if author.bot == True:
        #stop bot from responding
        return

    #get 20 latest tweets from @dog_feelings and add them to a dict
    t = api.GetUserTimeline(screen_name="dog_feelings", count=20)
    tweets = [i.AsDict() for i in t]

    #if message starts with 'hello doggo', say hello and @ the person who said it
    if text.startswith('hello doggo'):
        msg = 'Henlo {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if (text.startswith('help doggo') or text.startswith('doggo help')):
        msg = "what are you thinking doggo? - Doggo will let you know what its thinking about\ndoggo show me a doggo - Doggo will send you a picture of a doggo\
        \ndoggo rate my doggo - if an image is attached doggo will rate it\
        \n\n***If you have an issue with the bot please contact tinyman1199#6969***"

        await message.channel.send(msg)

    #if message starts with 'what are you thinking doggo?'
    if text.startswith('what are you thinking doggo?'):
        #get random tweet from the dict of tweets
        msg = tweets[random.randint(0,20)]['full_text']
        #send tweet as message
        await message.channel.send(msg)

    #if message starts with 'doggo show me a doggo' send a pic of a doggo from folder
    if text.startswith('doggo show me a doggo'):
        decision = random.randint(0,100)
        if (decision < 26):
            #get list of files
            l = os.listdir(dir_path+'/Doggos')
            number_files = len(l)
            #get random number for image
            rando = random.randint(1,number_files)
            #send the file
            path = dir_path+'/Doggos/'+l[rando-1]
            m = await channel.send(file=discord.File(path))
        else:
            with urllib.request.urlopen("https://dog.ceo/api/breeds/image/random") as url:
                data = json.loads(url.read().decode())
                url = data['message']
            urllib.request.urlretrieve(url, dir_path + "//doggo.png")
            path = dir_path+'//doggo.png'
            m = await channel.send(file=discord.File(path))
            os.remove(dir_path + "//doggo.png")
        await m.add_reaction("❤")

    #if "test" in text:
    #    embed = discord.Embed();
    #    embed.set_thumbnail(url='https://images.dog.ceo/breeds/chow/n02112137_5089.jpg')
    #    await message.channel.send(embed=embed)

    #if some asks 'doggo rate my doggo' and they have a file
    if text.startswith('doggo rate my doggo') and message.attachments[0]:
        #if attached file is an image
        for i in pic_ext:
            if (message.attachments[0].filename).endswith(i):
                #react with a heart to the image they sent
                await message.add_reaction("❤")
                #get random numbers for rating and message responce
                choice = random.randint(0,len(rate)-1)
                rating = random.randint(10,21)
                #reply with at least 10/10 and a random message from list
                msg = str(rating) + "/10 " + rate[choice]
                await message.channel.send(msg)

    #if message contains 'good boy' or 'good boi'
    if "good boy" in text or "good boi" in text:
        #reply with 'im a good boy'
        await message.channel.send('im a good boy')

    #if message contains 'woof'
    if "woof" in text:
        #reply with 'bork' and vice versa
        await message.channel.send('bork')

    if "bork" in text:
        await message.channel.send('woof')

    #if message contains 'cat'
    if "cat" in text:
        #reply with 'WOOF! BORK WOOF!'
        await message.channel.send('WOOF! BORK! WOOF!')

    #at random send a message of 'woof woof' or 'bork bork'
    if rand == 50:
        await message.channel.send('woof woof')

    if rand == 20:
        await message.channel.send('bork bork')



@client.event
#log basic info when the bot starts running
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
