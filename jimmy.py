import discord
import random
import requests
import json
import functions    # Separate py doc with functions
import os

from dotenv import load_dotenv
from serpapi import GoogleSearch

TOKEN = 'OTg0NTExODg0MzIzNjA2NTc4.GYOPBV.PejGVUEdKxNGl63DlzCDmOqzIFWumx-A1CzvzU'
# dogs = ['https://www.rd.com/wp-content/uploads/2021/01/GettyImages-588935825.jpg',
#     'https://cdn2.psychologytoday.com/assets/styles/manual_crop_1_91_1_1528x800/public/field_blog_entry_teaser_image/PT_dog_pic_cover_0.png.jpg?itok=wnWCDUk2']

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
        search_param = user_message.split(" ")[1:]
        search_param_concat = ""

        for x in search_param:
            search_param_concat += x + " "

        print(search_param_concat)
        search_dict = {"q": search_param_concat,
            "tbm": "isch",
            "ijn": "0",
            "api_key": "ce8ea31a80800c7255235d8d5b2e3a87e475a463f7bd5c6800bdd06a3f23a900"
        }

        search = GoogleSearch(search_dict)
        results = search.get_dict()
        image_results = results["images_results"]
        image_ret = [x["original"] for x in image_results]
        await message.channel.send(random.choice(image_ret))

    if user_message.startswith('!quote') or user_message.startswith('!q'):
        quote = functions.get_quote()
        await message.channel.send(quote)

    if user_message.startswith('!yomama'):
        joke = functions.yo_mama()
        await message.channel.send(joke)

client.run(TOKEN)
