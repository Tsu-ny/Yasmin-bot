import os
from discord.ext import commands
from pathlib import Path

class CogManager:
    """Classe para gerenciar todos os Cogs do bot."""

    def __init__(self, bot, cog_folder=None):
        self.bot = bot
        # Caminho dos Cogs
        if cog_folder is None:
            self.cog_folder = Path(__file__).parent / "cogs"
        else:
            self.cog_folder = Path(cog_folder).resolve()
        # Lista de módulos carregados
        self.loaded_cogs = []
  
    def discover_cogs(self):
        """Retorna uma lista de todos os módulos de Cogs encontrados recursivamente."""
        cogs = []
        for file_path in self.cog_folder.rglob("*.py"):
            if not file_path.name.startswith("__"):
                # módulo no formato config.cogs.subfolder.more_commands
                # converte caminho em módulo Python
                relative_path = file_path.relative_to(Path(__file__).parent.parent)
                module = ".".join(relative_path.with_suffix("").parts)
                cogs.append(module)
        return cogs

    async def load_all(self):
        """Carrega todos os Cogs encontrados."""
        for cog in self.discover_cogs():
            try:
                await self.bot.load_extension(cog)
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