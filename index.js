require("dotenv").config();

const express = require("express");
const { Client, GatewayIntentBits } = require("discord.js");

const app = express();
const PORT = process.env.PORT || 4000;
const TOKEN = process.env.DISCORD_TOKEN;

// Simple web server so Render is happy
app.get("/", (req, res) => {
  res.send("✅ Bot is running");
});

app.listen(PORT, () => {
  console.log(`🌐 Web server running on port ${PORT}`);
});

// Only use SAFE + DEFAULT intents
const client = new Client({
  intents: [GatewayIntentBits.Guilds] // No message, no members, no presences
});

client.once("ready", () => {
  console.log(`✅ Logged in as ${client.user.tag}`);
});

client.login(TOKEN);
