import discord
import random
import requests
import json
import functions    # Separate py doc with functions
import os

from dotenv import load_dotenv

TOKEN = 'OTg0NTExODg0MzIzNjA2NTc4.GYOPBV.PejGVUEdKxNGl63DlzCDmOqzIFWumx-A1CzvzU'

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

        image_ret = functions.google_image_search(search_param_concat)
        await message.channel.send(random.choice(image_ret))

    if user_message.startswith('!quote') or user_message.startswith('!q'):
        quote = functions.get_quote()
        await message.channel.send(quote)

    if user_message.startswith('!yomama'):
        joke = functions.yo_mama()
        await message.channel.send(joke)

client.run(TOKEN)
