import os
import discord
from discord.ext import tasks

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("DISCORD_TOKEN is not set in environment variables")

# Use only default intents, no message content, members, or presences
intents = discord.Intents.default()

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")
    keep_alive.start()  # start a dummy task to keep the bot busy

# Optional dummy task just to stay active
@tasks.loop(minutes=5)
async def keep_alive():
    print("⏱ Bot is still running...")

bot.run(TOKEN)
