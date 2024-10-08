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
                name=class_data[i][0],
                image=class_data[i][1]
            )
            await message.guild.create_role(
                name=class_data[i][2],
                color=discord.Colour.from_str(class_data[i][3])
            )

    if message.content == '/start-here':
        """Generate start here category with role-assign channel."""
        overwrites={
            message.guild.default_role: discord.PermissionOverwrite(add_reactions=False)
        }
        category = await message.guild.create_category(
            name='Start Here'
        )
        await category.edit(position=0) # would not set to pos 0 when setting in create_category()
        channel = await message.guild.create_text_channel(
            name='role-assign',
            overwrites=overwrites,
            category=category
        )
        class_msg = await channel.send("React with your class")
        class_emojis = []
        for i in range(num_classes):
            emoji = discord.utils.find(lambda e: e.name == class_data[i][0], channel.guild.emojis)
            class_emojis.append(emoji)
        for i in range(num_classes):
            await class_msg.add_reaction(class_emojis[i])
        

client.run(os.getenv("BOT_LOGIN_TOKEN"))