import discord
from discord.ext import commands

class MemberInfo(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot: discord.Client = bot

    @commands.command()
    async def account_age(self, ctx, *, member = None):
        member = member or ctx.author

        await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


async def setup(bot):
    await bot.add_cog(MemberInfo(bot))

