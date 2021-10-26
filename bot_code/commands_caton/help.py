with open("../bot_code/commands_caton/variables/help.txt") as text:
    help = text.readlines()
    text.close()
    
async def execute(client, message, args, command, prefix):
    await message.channel.send(message.author.mention + " I sent you the help.")
    await message.author.send(" ".join(help))