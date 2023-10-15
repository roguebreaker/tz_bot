import asyncio
import os
import discord
import requests
import json
import sys
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get

TZ_ID_TO_STRING = {
    17: "Burial Grounds</br>Crypt</br>Mausoleum",
    33: "Cathedral</br>Catacombs",
    3: "Cold Plains</br>Cave",
    5: "Darkwood</br>Underground Passage",
    2: "Blood Moor</br>Den of Evil",
    28: "Jail</br>Barracks",
    39: "Moo Moo Farm",
    4: "Stony Field",
    6: "Black Marsh</br>The Hole",
    20: "Forgotten Tower",
    12: "Pit",
    38: "Tristram",
    47: "Lut Gholein Sewers",
    41: "Stony Tomb</br>Rocky Waste",
    42: "Dry Hills</br>Halls of the Dead",
    43: "Far Oasis",
    44: "Lost City</br>Valley of Snakes</br>Claw Viper Temple",
    65: "Ancient Tunnels",
    66: "Tal Rasha's Tombs",
    74: "Arcane Sanctuary",
    76: "Spider Forest</br>Spider Cavern",
    77: "Great Marsh",
    78: "Flayer Jungle and Dungeon",
    80: "Kurast Bazaar</br>Temples",
    83: "Travincal",
    100: "Durance of Hate",
    104: "Outer Steppes</br>Plains of Despair",
    106: "City of the Damned</br>River of Flame",
    108: "Chaos Sanctuary",
    110: "Bloody Foothills</br>Frigid Highlands</br>Abbadon",
    112: "Arreat Plateau</br>Pit of Acheron",
    113: "Crystalline Passage</br>Frozen River",
    121: "Nihlathak's Temple and Halls",
    115: "Glacial Trail</br>Drifter Cavern" ,
    118: "Ancient's Way</br>Icy Cellar",
    128: "Worldstone Keep</br>Throne of Destruction</br>Worldstone Chamber",
}

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    url = 'https://www.d2emu.com//api/v1/tz'
    channel = client.get_channel(1070419768508678236)

    response = requests.get(url)
    my_json = json.loads(response.text)
    current_id = my_json['current'][0]
    next_id = my_json['next'][0]
    current = TZ_ID_TO_STRING[int(current_id)].replace('</br>', ', ')
    next = TZ_ID_TO_STRING[int(next_id)].replace('</br>', ', ')
    tz_message = f'Current TZ: {current}\n\nNext TZ: {next}'
    for zone in ['Chaos Sanctuary', 'Worldstone Keep', 'Tal Rasha\'s Tombs']:
        if zone in tz_message:
            tz_message = '<@&1070138319217905734> <@&1070138494476881991> \n' + tz_message
            break
    await channel.send(tz_message)
    sys.exit(0)

client.run(TOKEN)
