async def execute(client, message, args, command, prefix):
    #ADD PERMISSION#
    de = int(args[0])
    await message.channel.purge(limit=de + 1, bulk = True)
