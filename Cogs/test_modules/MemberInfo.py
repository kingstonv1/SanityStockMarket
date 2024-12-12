import discord
from discord.ext import commands

class MemberInfo(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot: discord.Client = bot

    @commands.command()
    async def account_age(self, ctx, *, member: discord.User):
        await ctx.send(f'{member.name} opened an account with us on {discord.utils.format_dt(member.joined_at)}.')

    @commands.command()
    async def account_name(self, ctx, *, member: discord.User):
        await ctx.send(f'Your username is {member.name}.')

    @commands.command()
    async def is_owner(self, ctx, *, member: discord.User):
        owner = await self.bot.is_owner(member)
        await ctx.send(f'{member.name} {"is" if owner else "is not"} a bank executive.')

async def setup(bot):
    await bot.add_cog(MemberInfo(bot))

