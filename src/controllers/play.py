async def play(ctx, query):
    if not query:
        return await ctx.send("You need to send me a request or youtube URL!")

    if ctx.author.voice:
        channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await ctx.send("Entered channel")
            await channel.connect()
    else:
        return await ctx.send("You need to be in a voice channel first!")

    if ctx.voice_client:
        source = discord.FFmpegPCMAudio(f"{cur_dir}/output/audio.m4a", executable="ffmpeg")

        # Cancel any previous inactivity check for this guild
        if ctx.guild.id in inactivity_tasks:
            inactivity_tasks[ctx.guild.id].cancel()

        def after_playing(error):
            #Runs after the audio stops playing (executed in a separate thread).
            if error:
                print(f"Error occurred: {error}")

            # Schedule the latest inactivity check
            task = bot.loop.create_task(check_inactivity(ctx.voice_client, ctx.guild.id))
            inactivity_tasks[ctx.guild.id] = task

        ctx.voice_client.play(source, after=after_playing)