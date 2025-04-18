import asyncio
from functions.QueueManager import get_inactivity_queue

inactivity_tasks = get_inactivity_queue()

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


def clear_last_inactivity_check(ctx):
    # Cancel any previous inactivity check for this guild
        if ctx.guild.id in inactivity_tasks:
            inactivity_tasks[ctx.guild.id].cancel()


async def user_in_channel(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await ctx.send("Entered channel")
            await channel.connect()
            return "Connected to the voice channel!"
    else:
        await ctx.send("You need to be in a voice channel first!")


