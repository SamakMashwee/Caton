async def execute(client, message, args, command, prefix):
    #ADD PERMISSION#
    de = int(args[0])
    if de > 100:
        await message.delete()
        await message.channel.send("You may not delete more than 100 messages you cumstack")
    elif de < 0:
        await message.delete()
        await message.channel.send("NO NEGATIVE NUMBERS NOW GIBE GOOD NUMBER")
    else:    
        await message.channel.purge(limit=de + 1, bulk = True)
