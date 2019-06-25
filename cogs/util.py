from discord.ext import commands
from discord.ext.commands import Context, Bot
from discord import Embed, Colour, Message
from typing import NoReturn


class Util(commands.Cog):
    """Commands for utilities related to discord or bot."""

    def __init__(self, bot: Bot) -> NoReturn:
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: Context) -> Message:
        """Responds with websocket latency"""
        embed = Embed(
            title="wew!",
            description=f"Pong!",
            colour=Colour.blue(),
        )
        return await ctx.send(embed=embed)


def setup(bot: Bot) -> None:
    bot.add_cog(Util(bot))
