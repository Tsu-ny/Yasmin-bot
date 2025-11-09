from discord.ext import commands
import random

class ChatCommands(commands.Cog):
    """Comandos de chat e interação"""
    
    def __init__(self, bot):
        self.bot = bot
        self._emoji = []
    
    # Cute emoji property
    @property
    def emoji(self):
        '''Returns a emoji that avoids immediate repetition.'''
        emoji = ['UwU', 'OwO', 'TwT', ':3', '>W<', '^-^', '>-<']
        options = [e for e in emoji if not self._emoji]
        
        if not options:
            self._emoji.clear()
            options = emoji

        choice = random.choice(options)
        self._emoji.append(choice)

        if len(self._emoji) > len(self._emoji) - 2:
            self._emoji.pop(0)
        
        return ' ' + choice
    
    @commands.command()
    async def say(self, ctx, *, mensagem):
        """Repete a mensagem com um emoji fofo
        
        Uso: .say <mensagem>
        """
        await ctx.send(mensagem + self.emoji)
        await ctx.message.delete()

async def setup(bot):
    await bot.add_cog(ChatCommands(bot))