# The sanity engine makes calls to OpenAI's API to evaluate the reasonability level of a message or collection of messages.

from discord.ext import commands
from pydantic import BaseModel
import openai

class SanityEngine(commands.Cog):
    class SanityRating(BaseModel):
        sanity_score: int

    def __init__(self, bot, openai_key) -> None:
        self.bot = bot
        self.llm = openai.OpenAI(api_key = openai_key, project = "proj_WqieGD8XWnfSKLpa0o4cjIpx")

    def setup(self, bot):
        self.bot.add_cog(SanityEngine(bot, self.key))

    async def eval_message_sanity(self, message):
        llm_response = self.llm.responses.parse(
            model = "gpt-4.1-mini",

            input = [
                {
                    "role": "system",
                    "content": """You work as a content moderator. Your job is to rate the mental state of a platform user given a message or series of messages provided, 
                    on a percentage scale of 1 to 100. 
                    If given context, consider whether the message is reasonable given the context. 
                    If not given context, rate the message as if a person came up to you and randomly said the contents of the message to you. 
                    Be sure to consider what kind of information the message reveals about the user.
                    Reply with nothing except your final rating number.
                    Do not gravitate towards multiples of 5 in your rating.
                    """
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
            
            text_format = self.SanityRating,
            temperature = 0
        )

        return llm_response.output_parsed.sanity_score
