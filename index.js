require("dotenv").config();
const express = require("express");
const { Client, GatewayIntentBits } = require("discord.js");

const app = express();
const PORT = process.env.PORT || 4000;
const TOKEN = process.env.DISCORD_TOKEN;

// --- WEB SERVER (Keep-alive) ---
app.get("/", (req, res) => {
  res.send("✅ Bot is running");
});

app.listen(PORT, () => {
  console.log(`🌐 Web server running on port ${PORT}`);
});

// --- DISCORD BOT ---
const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent
  ]
});

client.once("ready", () => {
  console.log(`✅ Logged in as ${client.user.tag}`);
});

// Event Listener: Respond to messages
client.on("messageCreate", (message) => {
  // 1. Ignore messages from bots (prevents infinite loops)
  if (message.author.bot) return;


  
});

// Global error handling to prevent crash
process.on('unhandledRejection', error => {
  console.error('Unhandled promise rejection:', error);
});

client.login(TOKEN);
