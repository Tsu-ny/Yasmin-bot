import discord
from discord.ext import commands
import random

class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._emoji = []
    
    # Cute emoji property
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
    
    # Repeat message saying and erase the message
    @commands.command()
    async def say(self, ctx, *, mensagem):
        await ctx.send(mensagem + self.emoji)
        await ctx.message.delete()

    @commands.command()
    async def d20(self, ctx):
        roll = random.randint(1, 20)
        await ctx.send(f'`{roll}`')

    # Clear messages
    @commands.command()
    async def clear(self, ctx, quantidade: int):
        deleted = await ctx.channel.purge(limit=quantidade)
        await ctx.send(f'Apaguei `{len(deleted)}` mensagens{self.emoji}', delete_after=5)

    # Ares-kun :3
    @commands.command()
    async def ares(self, ctx):
        ares = ['Ares?! Eu amo muito ele!!!', 'Ares é meu crush secreto <3', 'Ares é tão fofo!!!', 'Ares é meu baby <3', 'Ares é meu rei!!!', 'Ares é tudo pra mim!!!', 'Sim, eu sou gamadinha nele UwU']
        # await ctx.send('Afis, ele ta jogando ;-;')
        await ctx.send(random.choice(ares))


    @commands.command(name='pm')
    async def pm(self, ctx, *, mensagem: str):
        """Envia mensagem privada (DM) para quem chamou o comando.

        Uso: .pm <mensagem>
        """
        try:
            await ctx.author.send(mensagem)
            # Tenta adicionar reação como confirmação (silencioso se falhar)
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
        """Envia DM para um usuário mencionado.

        Uso: .dm @usuario <mensagem>
        """
        try:
            await user.send(mensagem)
            await ctx.message.delete()
            await ctx.send(f"Enviei uma DM para {user.mention} >:3", delete_after=6)
        except discord.Forbidden:
            await ctx.send(f"Não consegui enviar DM para {user.mention}. Talvez esteja com a DM fechada :/", delete_after=8)
        except Exception as e:
            await ctx.send(f"Erro ao enviar DM para {user.mention}: {e}", delete_after=8)


    # List all commands
    @commands.command()
    async def h(self, ctx):
        help_message = (
            "Aqui estão os comandos disponíveis:\n"
            '------------------------------------------------\n'
            "`.say <mensagem>` - Repete a mensagem.\n"
            "`.clear <quantidade>` - Apaga a quantidade especificada de mensagens do canal.\n"
            "`.pm <mensagem>` - Envia uma DM para você.\n"
            "`.dm @usuario <mensagem>` - Envia uma DM para o usuário mencionado.\n"
            "`.h` - Mostra esta mensagem, óbvio."
        )
        await ctx.send(help_message)