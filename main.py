import json

import discord
from discord.ext import commands

from Cogs.admin_commands.Tree import Tree
from Cogs.test_modules.MemberInfo import MemberInfo
from Cogs.Core.MessageEvaluation import MessageEvaluation
from Cogs.Core.SanityEngine import SanityEngine

# Get configuration.json
with open("configuration.json", "r") as config: 
    data = json.load(config)
    token = data["token"]
    prefix = data["prefix"]
    owner_id = data["owner_id"]
    openai_key = data["openai_key"]

# Intents
intents = discord.Intents.default()
intents.message_content = True
# The bot
bot = commands.Bot(prefix, intents = intents, owner_id = owner_id)

async def load_cogs():
    await bot.add_cog(Tree(bot))
    await bot.add_cog(MemberInfo(bot))
    await bot.add_cog(SanityEngine(bot, openai_key))
    await bot.add_cog(MessageEvaluation(bot))


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await load_cogs()
    # await bot.tree.sync(guild=bot.get_guild(1219773166600196116))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{bot.command_prefix}help. Seeking employment :("))

bot.run(token)
