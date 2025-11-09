import discord
from discord.ext import commands
from typing import List
from config.cogs import CogManager

class MyBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)
        # Cria o gerenciador de Cogs
        self.cog_manager = CogManager(self, cog_folder='cogs')

    async def on_ready(self):
        print(f'Bot online como {self.user}')
        
        # Envie uma mensagem de teste para você mesmo ao iniciar o bot
        user = await self.fetch_user(572812140143181825)
        await user.send("Tô on!! UwU")

        # Define a presença do bot
        await self.change_presence(activity=discord.Game(name=""))
        await self.change_presence(status=discord.Status.online)

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Comando não encontrado ;-;\nUse `.h` para ver a lista de comandos disponíveis ;3")

    async def setup_hook(self):
        """Carrega todos os Cogs quando o bot inicia"""
        loaded_cogs = self.cog_manager.load_all()
        print(f"Cogs carregados: {', '.join(loaded_cogs) if loaded_cogs else 'Nenhum'}")

    async def reload_all_cogs(self) -> List[str]:
        """Recarrega todos os Cogs atualmente carregados"""
        reloaded_cogs = []
        
        for extension in list(self.extensions):
            try:
                await self.reload_extension(extension)
                reloaded_cogs.append(extension)
            except Exception as e:
                print(f"Erro ao recarregar o Cog {extension}: {str(e)}")
        
        return reloaded_cogs