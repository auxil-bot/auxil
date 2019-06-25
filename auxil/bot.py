from discord.ext.commands import AutoShardedBot
from discord import Message
from os import getenv
from typing import List
import traceback
import sys
initial_extensions = [
    "cogs.util"
]

def _get_prefix(bot: AutoShardedBot, message: Message) -> List[str]:
    base = [f"<@!{bot.user.id}> ", f"<@{bot.user.id}> "]
    if message.guild is None:
        base.append("")
    else:
        # TODO
        prefixes = getenv("PREFIX")
        base.append(prefixes)
    return base

description = """
TODO
"""


class Auxil(AutoShardedBot):
    def __init__(self) -> None:
        super().__init__(command_prefix=_get_prefix, description=description)
        for extension in initial_extensions:
            try:
                self.load_extension(extension)
            except Exception as e:
                print(f'Failed to load extension {extension}.', file=sys.stderr)
                traceback.print_exc()

    async def on_ready(self) -> None:
        print(f"Aye, {self.user.name} is ready to spread the support!")
    async def on_message(self, message: Message) -> None:
        if message.author.bot:
            return
        await self.process_commands(message)
    async def close(self) -> None:
        await super().close()

    def run(self):
        try:
            super().run(getenv("TOKEN"), reconnect=True)
        finally:
            print("wew")
