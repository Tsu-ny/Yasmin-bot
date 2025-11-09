from discord.ext import commands

class ModCommands(commands.Cog):
    """Comandos de moderação do servidor"""
    
    def __init__(self, bot):
        self.bot = bot
    
    # Clear messages
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, quantidade: int):
        """Apaga uma quantidade específica de mensagens do canal
        
        Uso: .clear <quantidade>
        Requer: Permissão para gerenciar mensagens
        """
        deleted = await ctx.channel.purge(limit=quantidade)
        await ctx.send(f'Apaguei `{len(deleted)}` mensagens', delete_after=5)
    
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Você não tem permissão para apagar mensagens ;-;", delete_after=5)

    @commands.command()
    async def h(self, ctx):
        """Mostra a lista de comandos disponíveis
        
        Uso: .h
        """
        help_message = (
            "Aqui estão os comandos disponíveis:\n\n"
            "__Comandos de Chat:__\n"
            "`.say <mensagem>` - Repete a mensagem digitada\n\n"
            "__Comandos de RPG:__\n"
            "`.d20` - Rola um dado de 20 lados\n\n"
            "__Comandos de Moderação:__\n"
            "`.clear <quantidade>` - Apaga a quantidade especificada de mensagens do canal\n"
            "`.h` - Testa ai pra tu ver >:3\n"
        )
        await ctx.send(help_message)

async def setup(bot):
    """Função necessária para carregar o Cog"""
    await bot.add_cog(ModCommands(bot))