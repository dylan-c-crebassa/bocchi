import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

from controllers.play import play

cur_dir= os.path.dirname(os.path.abspath(__file__))

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Enable required intents
intents = discord.Intents.default()
intents.message_content = True  # Required to read commands

# Initialize bot with command prefix
bot = commands.Bot(command_prefix="!", intents=intents)

# Dictionary to track inactivity tasks per guild
inactivity_tasks = {}

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    #A simple command that replies with a greeting.
    await ctx.send(f"Hello, {ctx.author.mention}! 😊")

@bot.command()
async def play(ctx, *, query: str = ""):
    play(ctx, query)
        

async def check_inactivity(voice_client, guild_id):
    #Checks if the bot is inactive and disconnects after 3 minutes.
    print(f"Starting inactivity timer for guild {guild_id}...")
    
    try:
        await asyncio.sleep(180)  # Wait 3 minutes
        if not voice_client.is_playing():  # If still not playing, disconnect
            print(f"Disconnecting from guild {guild_id} due to inactivity.")
            await voice_client.disconnect()
    except asyncio.CancelledError:
        print(f"Inactivity check for guild {guild_id} was cancelled.")
    finally:
        inactivity_tasks.pop(guild_id, None)  # Remove from dictionary


# Run the bot
bot.run(TOKEN)
