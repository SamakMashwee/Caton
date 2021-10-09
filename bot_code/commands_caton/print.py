async def execute(client, message, args, command, prefix):
    await message.channel.send(message.content.lstrip(prefix+command))