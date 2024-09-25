import discord, os
from dotenv import load_dotenv
from utility import class_data, num_classes

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
    
    if message.content == '/generate-classes':
        """Generate class emojis and roles."""
        for i in range(num_classes):
            await message.guild.create_custom_emoji(
                name="wow_" + class_data[i][0],
                image=class_data[i][3]
            )
            await message.guild.create_role(
                name=class_data[i][1],
                color=discord.Colour.from_str(class_data[i][2])
            )
        

client.run(os.getenv("BOT_LOGIN_TOKEN"))