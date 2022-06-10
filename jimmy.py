import discord
import random
import requests
import json
import functions    # Separate py doc with functions

import os
from dotenv import load_dotenv

TOKEN = 'OTg0NTExODg0MzIzNjA2NTc4.GYOPBV.PejGVUEdKxNGl63DlzCDmOqzIFWumx-A1CzvzU'
dogs = ['https://www.rd.com/wp-content/uploads/2021/01/GettyImages-588935825.jpg',
    'https://cdn2.psychologytoday.com/assets/styles/manual_crop_1_91_1_1528x800/public/field_blog_entry_teaser_image/PT_dog_pic_cover_0.png.jpg?itok=wnWCDUk2']

client = discord.Client()

load_dotenv()
TOKEN = os.getenv("TOKEN")

@client.event
async def on_ready():
    print('{0.user} online >:)'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if user_message.startswith('!help'):
        help = functions.help()
        await message.channel.send(help)

    if user_message.startswith('!pic'):
        await message.channel.send(random.choice(dogs))

    if user_message.startswith('!quote') or user_message.startswith('!q'):
        quote = functions.get_quote()
        await message.channel.send(quote)

    if user_message.startswith('!yomama'):
        joke = functions.yo_mama()
        await message.channel.send(joke)

client.run(TOKEN)
