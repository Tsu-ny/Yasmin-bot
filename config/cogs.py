import os
from discord.ext import commands

class CogManager:
    """Classe para gerenciar todos os Cogs do bot."""

    def __init__(self, bot, cog_folder='cogs'):
        self.bot = bot
        # Caminho absoluto da pasta de Cogs
        self.cog_folder = os.path.join(os.path.dirname(__file__), cog_folder)
        # Lista de módulos carregados
        self.loaded_cogs = []

    def discover_cogs(self):
        """Retorna uma lista de todos os módulos de Cogs encontrados recursivamente."""
        cogs = []
        for root, dirs, files in os.walk(self.cog_folder):
            for file in files:
                if file.endswith('.py') and not file.startswith('__'):
                    relative_path = os.path.relpath(os.path.join(root, file), start=os.path.dirname(__file__))
                    module = relative_path.replace(os.sep, ".").replace(".py", "")
                    cogs.append(module)
        return cogs

    def load_all(self):
        """Carrega todos os Cogs encontrados."""
        for cog in self.discover_cogs():
            try:
                self.bot.load_extension(cog)
                self.loaded_cogs.append(cog)
                print(f"Cog carregado: {cog}")
            except commands.ExtensionAlreadyLoaded:
                print(f"Cog {cog} já estava carregado.")
            except commands.NoEntryPointError:
                print(f"Cog {cog} não tem setup(bot), ignorando.")
            except Exception as e:
                print(f"Erro ao carregar {cog}: {e}")

        return self.loaded_cogs

    def unload_all(self):
        """Descarrega todos os Cogs carregados."""
        for cog in list(self.loaded_cogs):
            try:
                self.bot.unload_extension(cog)
                self.loaded_cogs.remove(cog)
                print(f"Cog descarregado: {cog}")
            except Exception as e:
                print(f"Erro ao descarregar {cog}: {e}")

    def reload_all(self):
        """Recarrega todos os Cogs carregados."""
        for cog in list(self.loaded_cogs):
            try:
                self.bot.reload_extension(cog)
                print(f"Cog recarregado: {cog}")
            except Exception as e:
                print(f"Erro ao recarregar {cog}: {e}")
