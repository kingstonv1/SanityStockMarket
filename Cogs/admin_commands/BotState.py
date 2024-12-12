import discord
import os
from discord.ext import commands

class BotState(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot: discord.Client = bot

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx):
        for item in [name for name in os.listdir("Cogs") if os.path.isdir(f'./Cogs/{name}')]:
            for filename in os.listdir(f'./Cogs/{item}'):
                if filename.endswith(".py"):
                   await self.bot.reload_extension(f"Cogs.{item}.{filename[:-3]}")  # type: ignore

        print(f'Extension reload requested by {ctx.author.name} completed.')
        await ctx.send(f'Extensions reloaded. Will that be all?')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("Sorry. Only bank executives can make that call.")
            return

        print(f"An error occurred: {error}")

async def setup(bot):
    await bot.add_cog(BotState(bot))

