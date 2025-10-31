import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from Classes.MyBot import MyBot

def main():
    # Importa as info do .env
    load_dotenv()

    #Tokens
    TOKEN = os.getenv("DISCORD_KEY")

    # Configuração básica
    intents = discord.Intents.default()
    intents.message_content = True  # Necessário para ler mensagens

    bot = MyBot(command_prefix='.', intents=intents)

    # Substitua pelo seu token real
    bot.run(TOKEN)

if __name__ == "__main__":
    main()