import discord, os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    """Log bot connection confirmation to console."""
    print(f"{client.user} successfully connected")

@client.event
async def on_message(message):
    """Setup slash commands."""

    if message.author == client.user:
        """Ignore messages from the bot."""
        return
    
    if message.content.startswith('/hello'):
        await message.channel.send("howdy!")

client.run(os.getenv("BOT_LOGIN_TOKEN"))