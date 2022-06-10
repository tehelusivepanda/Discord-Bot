import discord
import random
import requests
import json

TOKEN = 'OTg0NTExODg0MzIzNjA2NTc4.GYOPBV.PejGVUEdKxNGl63DlzCDmOqzIFWumx-A1CzvzU'
dogs = ['https://www.rd.com/wp-content/uploads/2021/01/GettyImages-588935825.jpg',
    'https://cdn2.psychologytoday.com/assets/styles/manual_crop_1_91_1_1528x800/public/field_blog_entry_teaser_image/PT_dog_pic_cover_0.png.jpg?itok=wnWCDUk2']

client = discord.Client()

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = '\"\"' + json_data[0]['q'] + '\" \n\t-' + json_data[0]['a'] + '\" \n\t\t-' + 'Jimmy'
    return(quote)

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

    if user_message.startswith('!hello'):
        await user_message.send('Hello!')

    if user_message.startswith('!pic'):
        await user_message.send(random.choice(dogs))

    if user_message.startswith('!quote') or user_message.startswith('!q'):
        quote = get_quote()
        await message.channel.send(quote)

client.run(TOKEN)
