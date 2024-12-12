import discord
from discord.ext import commands
import json
import os

# Get configuration.json
with open("configuration.json", "r") as config: 
	data = json.load(config)
	token = data["token"]
	prefix = data["prefix"]

# Intents
intents = discord.Intents.default()
intents.message_content = True
ownerids = set([546827180404113426, 1169402249668206735])
# The bot
bot = commands.Bot(prefix, intents = intents, owner_ids = ownerids)

async def load_cogs():
    for item in [name for name in os.listdir("Cogs") if os.path.isdir(f'./Cogs/{name}')]:
        for filename in os.listdir(f'./Cogs/{item}'):
            if filename.endswith(".py"):
               await bot.load_extension(f"Cogs.{item}.{filename[:-3]}")  # type: ignore
               print(f'Loaded extension {filename}')


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    print(discord.__version__)
    await load_cogs()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{bot.command_prefix}help"))

bot.run(token)
