import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

from controllers.play import PlayController

cur_dir= os.path.dirname(os.path.abspath(__file__))

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Enable required intents
intents = discord.Intents.default()
intents.message_content = True  # Required to read commands

# Initialize bot with command prefix
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    #A simple command that replies with a greeting.
    await ctx.send(f"Hello, {ctx.author.mention}! 😊")

@bot.command()
async def play(ctx, *, query: str = ""):
    PlayController(bot, ctx, query)
        


# Run the bot
bot.run(TOKEN)
