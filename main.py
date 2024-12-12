import discord
from discord.ext import commands
import json
import os

# Get configuration.json
with open("configuration.json", "r") as config: 
	data = json.load(config)
	token = data["token"]
	prefix = data["prefix"]
	owner_id = data["owner_id"]

# Intents
intents = discord.Intents.default()
intents.message_content = True
# The bot
bot = commands.Bot(prefix, intents = intents, owner_id = owner_id)

async def load_cogs():
    folders = []
    for item in os.listdir("Cogs"):
        if os.path.isdir(f'./Cogs/{item}'):
            folders.append(item)

    for item in folders:
        for filename in os.listdir(f'./Cogs/{item}'):
            if filename.endswith(".py"):
               await bot.load_extension(f"Cogs.{item}.{filename[:-3]}")  # type: ignore
               print(f'Loaded extension {filename}')
     

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    print(discord.__version__)
    await load_cogs()
    bot.tree.copy_global_to(guild=bot.get_guild(1219773166600196116))
    await bot.tree.sync(guild=bot.get_guild(1219773166600196116))
    print('Synced Tree!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{bot.command_prefix}help"))

bot.run(token)
