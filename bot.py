import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Use default intents WITHOUT privileged message_content
intents = discord.Intents.default()
intents.message_content = False  # Disable privileged intent

bot = commands.Bot(command_prefix="!", intents=intents)  # <-- make sure intents are passed here

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

bot.run(TOKEN)
