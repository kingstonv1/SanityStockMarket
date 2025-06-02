import discord
from discord.ext import commands

class MemberInfo(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    def setup(self, bot):
        self.bot.add_cog(MemberInfo(bot))

    @commands.command()
    async def account_age(self, ctx, *, member = None):
        member = member or ctx.author

        await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

