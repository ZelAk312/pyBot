import json
import discord
from os import path
from src.CommandHandler import CommandHandler

#To import json files
def importJSON(fileName):
    file = open(fileName, "r")
    return json.loads(file.read())

#Get config
config = importJSON(path.realpath("./config.json"))

#Get a client from discord.py
client = discord.Client()

#Get the commands
CommandHand = CommandHandler(client, config)

@client.event
async def on_ready():
    print(config["bot"]["loginMsg"])

@client.event
async def on_message(msg):
    if msg.author.id == client.user.id:
        await CommandHand.handle(msg)

#Login the bot
client.run(config["bot"]["token"], bot=False)