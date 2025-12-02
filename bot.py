import os
import discord
from discord.ext import tasks

# Get token from environment variables
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("DISCORD_TOKEN is not set in environment variables")

# Only default intents, no privileged intents
intents = discord.Intents.default()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")
    keep_alive.start()  # start dummy task to show activity

# Dummy task to keep the bot active
@tasks.loop(minutes=5)
async def keep_alive():
    print("⏱ Bot is still running...")

bot.run(TOKEN)
