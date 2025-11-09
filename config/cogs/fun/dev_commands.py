import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
import os


load_dotenv()

class DevCommands(commands.Cog):
    """Comandos exclusivos para o dev"""
    
    def __init__(self, bot):
        self.bot = bot
        self._emoji = []
        # Seu ID do Discord aqui
        self.dev_id = int(os.getenv("ID_DEV", "0")) # Este é o ID que vi sendo usado no bot.py
        # self.dev_id = 572812140143181825 # Este é o ID que vi sendo usado no bot.py
    
    def cog_check(self, ctx):
        """Verifica se quem chamou o comando é o dev"""
        return ctx.author.id == self.dev_id

    # Cute emoji property (copiado do fun para manter consistência)
    @property
    def emoji(self):
        '''Returns a emoji that avoids immediate repetition.'''
        emoji = ['UwU', 'OwO', 'TwT', ':3', '>W<', 'nwn', '^-^', '>-<']
        options = [e for e in emoji if not self._emoji]
        
        if not options:
            self._emoji.clear()
            options = emoji

        choice = random.choice(options)
        self._emoji.append(choice)

        if len(self._emoji) > len(self._emoji) / 2:
            self._emoji.pop(0)
        
        return ' ' + choice

    @commands.command()
    async def ares(self, ctx):
        """[DEV] Fala algo fofo sobre o Ares"""
        ares = ['Ares?! Eu amo muito ele!!!', 'Ares é meu crush secreto <3', 
                'Ares é tão fofo!!!', 'Ares é meu baby <3', 'Ares é meu rei!!!', 
                'Ares é tudo pra mim!!!', 'Sim, eu sou gamadinha nele UwU']
        await ctx.send(random.choice(ares))

    @commands.command(name='pm')
    async def pm(self, ctx, *, mensagem: str):
        """[DEV] Envia mensagem privada (DM) para quem chamou o comando"""
        try:
            await ctx.author.send(mensagem + self.emoji)
            try:
                await ctx.message.add_reaction('✉️')
            except Exception:
                pass
        except discord.Forbidden:
            await ctx.send("Não consegui te enviar DM — Talvez suas DMs estão fechadas :c", delete_after=8)
        except Exception as e:
            await ctx.send(f"Erro ao enviar DM: {e}", delete_after=8)

    @commands.command(name='dm')
    async def dm(self, ctx, user: discord.User, *, mensagem: str):
        """[DEV] Envia DM para um usuário mencionado"""
        try:
            await user.send(mensagem)
            # await user.message.delete()
            await ctx.send(f"Enviei uma DM para {user.mention}", delete_after=6)
        except discord.Forbidden:
            await ctx.send(f"Não consegui enviar DM para {user.mention}. Talvez esteja com DMs fechadas.", delete_after=8)
        except Exception as e:
            await ctx.send(f"Erro ao enviar DM para {user.mention}: {e}", delete_after=8)

    async def cog_command_error(self, ctx, error):
        """Handler para erros nos comandos deste Cog"""
        if isinstance(error, commands.CheckFailure):
            # Silenciosamente ignora tentativas de uso por não-devs
            await ctx.message.add_reaction('❌')
        else:
            # Log outros erros normalmente
            print(f"Erro no comando {ctx.command}: {error}")

async def setup(bot):
    await bot.add_cog(DevCommands(bot))