import discord
from discord.ext import commands
import Cogs.admin_commands.Tree
import Cogs.test_modules.MemberInfo
import json

# Get configuration.json
with open("configuration.json", "r") as config: 
	data = json.load(config)
	token = data["token"]
	prefix = data["prefix"]
	owner_id = data["owner_id"]

# Intents
intents = discord.Intents.default()
# The bot
bot = commands.Bot(prefix, intents = intents, owner_id = owner_id)

async def load_cogs():
    await bot.add_cog(Tree(bot))
    await bot.add_cog(MemberInfo(bot))


     

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    print(discord.__version__)
    await load_cogs()
    # await bot.tree.sync(guild=bot.get_guild(1219773166600196116))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{bot.command_prefix}help"))

bot.run(token)
