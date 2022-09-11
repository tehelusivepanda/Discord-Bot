import discord
import random
import requests
import json
import functions

from serpapi import GoogleSearch

def help():
    help_list = '''```List of usable commands with the Jimmy bot:\n
    -!q or !quote \t Generate an inspirational quote by Jimmy\n
    -!pic         \t Returns random image through Google search. (Format: !pic "YOUR SEARCH TERM HERE")\n
    -!yomama      \t Yo mama so...\n```'''
    return (help_list)

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = '\"\"' + json_data[0]['q'] + '\" \n\t-' + json_data[0]['a'] + '\" \n\t\t-' + 'Jimmy'
    return(quote)

def yo_mama():
    response = requests.get('https://yomomma-api.herokuapp.com/jokes')
    json_data = json.loads(response.text)
    print(json_data)
    joke = json_data['joke'] + ' :joy::joy::joy::joy_cat:'
    return(joke)

def google_image_search(search_param_concat):
        search_dict = {"q": search_param_concat,
            "tbm": "isch",
            "ijn": "0",
            "api_key": "ce8ea31a80800c7255235d8d5b2e3a87e475a463f7bd5c6800bdd06a3f23a900"
        }

        search = GoogleSearch(search_dict)
        results = search.get_dict()
        image_results = results["images_results"]
        image_ret = [x["original"] for x in image_results]
        return(image_ret)