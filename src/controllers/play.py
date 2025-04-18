
import discord

from functions.downloadAudio import format_query, allocate_queue
from helpers.play_utils import user_in_channel, clear_last_inactivity_check, check_inactivity
from functions.QueueManager import get_inactivity_queue, song_queue

inactivity_tasks = get_inactivity_queue()

async def PlayController(bot, ctx, url_or_query):
    if not url_or_query and song_queue.is_empty():
        return await ctx.send("You need to send me a request or youtube URL!")

    # Validate if user is in channel
    if not await user_in_channel(ctx):
        return

    allocate_queue(format_query(url_or_query))


    if ctx.voice_client:

        source = discord.FFmpegPCMAudio(f"../output/audio.m4a", executable="ffmpeg")

        clear_last_inactivity_check(bot, ctx)

        def after_playing(error):
            #Runs after the audio stops playing (executed in a separate thread).
            if error:
                print(f"Error occurred: {error}")

            # Schedule the latest inactivity check
            task = bot.loop.create_task(check_inactivity(ctx.voice_client, ctx.guild.id))
            inactivity_tasks[ctx.guild.id] = task
            next_task = bot.loop.create_task(PlayController(bot, ctx))


        ctx.voice_client.play(source, after=after_playing)

