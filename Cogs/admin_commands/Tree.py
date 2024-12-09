import discord
from discord.ext import commands

class Tree(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def sync_tree(self, ctx, *):
        await discord.app_commands.CommandTree.sync(*, guild = "1219773166600196116")

