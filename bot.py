import os
import time

import discord
from dotenv import load_dotenv

from handlers import dispatch, load_handlers

load_dotenv()
load_handlers()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    user = client.user
    if user is None:
        print("Discord client connected, but user is unavailable.")
        return
    print(f"{user.name} has connected to Discord!")


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Hi {member.name}, fuck you!")


# @client.event
# async def on_message_edit(before, after):
#     await after.guild.channels.send("edit")


@client.event
async def on_member_update(before, after):
    if before != after:
        for channel in after.guild.channels:
            if str(channel) == "general":
                await channel.send(f"{before.nick} has changed their name to {after.nick}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    with open("stats.txt", "a") as f:
        f.write(f"{int(time.time())}\n")

    await dispatch(message)


token = os.environ.get("TOKEN")
if not token:
    raise RuntimeError("TOKEN is not set. Add it to your .env file before running the bot.")

client.run(token)
