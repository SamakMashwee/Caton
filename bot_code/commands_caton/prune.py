import math
import discord

async def execute(client, message, args, command, prefix):
    await client.delete_messages([message for message in client.logs_from(message.channel, limit=int(args))])