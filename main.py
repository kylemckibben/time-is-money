import discord
from dotenv import load_dotenv
from utility import *

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

    if message.content == '/generate-class-emojis':
        """Generate class emojis on server."""
        class_icons = generate_class_icon_byteobjs()
        for i in range(len(class_names)):
            await message.guild.create_custom_emoji(
                name=class_names[i],
                image=class_icons[i]
            )

client.run(os.getenv("BOT_LOGIN_TOKEN"))