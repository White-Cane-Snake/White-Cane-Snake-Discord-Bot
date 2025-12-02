import os
import discord
from discord.ext import tasks
from flask import Flask
from threading import Thread

# ===== Web server just for Render =====
app = Flask("")

@app.route("/")
def home():
    return "Bot is alive!"

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 4000)))

# Start Flask in a separate thread
Thread(target=run_flask).start()

# ===== Discord Bot =====
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("DISCORD_TOKEN is not set in environment variables")

intents = discord.Intents.default()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")
    keep_alive.start()

# Dummy task to show activity
@tasks.loop(minutes=5)
async def keep_alive():
    print("⏱ Bot is still running...")

bot.run(TOKEN)
