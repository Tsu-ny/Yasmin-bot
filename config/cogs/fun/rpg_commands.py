from discord.ext import commands
import random

class RPGCommands(commands.Cog):
    """Comandos relacionados a RPG"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def d20(self, ctx):
        """Rola um dado de 20 lados
        
        Uso: .d20
        """
        roll = random.randint(1, 20)
        await ctx.send(f'`{roll}`')

async def setup(bot):
    await bot.add_cog(RPGCommands(bot))