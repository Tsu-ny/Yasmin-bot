import discord
from dotenv import load_dotenv
import os
from config.bot import MyBot

def main():
    # Importa as info do .env
    load_dotenv()

    #Tokens
    TOKEN = os.getenv("DISCORD_KEY")

    # Configuração básica
    intents = discord.Intents.default()
    intents.message_content = True  # Necessário para ler mensagens
    intents.members = True  # Necessário para eventos relacionados a membros

    bot = MyBot(command_prefix='.', intents=intents)

    bot.run(str(TOKEN))

if __name__ == "__main__":
    main()