import discord
from discord.ext import commands
from Classes.commands import BasicCommands

class MyBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)

    async def on_ready(self):
        print(f'Bot online como {self.user}')

    async def setup_hook(self):
        await self.add_cog(BasicCommands(self))