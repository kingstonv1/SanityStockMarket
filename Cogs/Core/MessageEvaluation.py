from discord.ext import commands
from pydantic import BaseModel
import openai

class MessageEvaluation(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    def setup(self, bot):
        self.bot.add_cog(MessageEvaluation(bot))

    @commands.command()
    async def how_sane(self, ctx, *, inp = None):
        message = None
        
        # if the context message is replying to another message, use that first
        if ctx.message.reference:
            message = ctx.message.reference.resolved.content
        # elif inp and is_link(inp):
            # todo: resolve message link into message, if it's formatted as a link
            pass
        elif inp:
            message = inp
        else:
            await ctx.send('Please use this command when replying to a message or supply a message to evaluate.')
        
        sanity_engine = self.bot.get_cog("SanityEngine")

        if not sanity_engine:
            print("Sanity Engine Not Loaded, in MessageEvaluation.how_sane command")
            await ctx.send("Sanity Engine cog isn't loaded. Report this bug.")
        
        res = await sanity_engine.eval_message_sanity(message)
        
        await ctx.send(f'The sanity rating of this message is {res}/100.')