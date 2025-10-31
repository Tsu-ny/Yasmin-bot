import discord
from discord.ext import commands
import random

class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @property
    def emoji(self):
        emoji = {
            'react' : ['UwU', 'OwO', '>:3', ':3'],
            'xd' : ['prrr', 'rawr', 'nya~']
            }
        return emoji

    @commands.command()
    async def say(self, ctx, *, mensagem):
        await ctx.send(mensagem + ' ' + random.choice(self.emoji['react']))

    @commands.command()
    async def d20(self, ctx):
        roll = random.randint(1, 20)
        await ctx.send(roll)

    @commands.command()
    async def clear(self, ctx, quantidade: int):
        deleted = await ctx.channel.purge(limit=quantidade)
        await ctx.send(f'Apaguei `{len(deleted)}` mensagens {random.choice(self.emoji)}', delete_after=5)

    @commands.command()
    async def ares(self, ctx):
        ares = ['Ares?! Eu amo muito ele!!!', 'Ares é meu crush secreto <3', 'Ares é tão fofo!!!', 'Ares é meu baby <3', 'Ares é meu rei!!!', 'Ares é tudo pra mim!!!', 'Sim, eu sou gamadinha nele UwU']
        # await ctx.send('Afis, ele ta jogando ;-;')
        await ctx.send(random.choice(ares))