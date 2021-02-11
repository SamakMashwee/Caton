import math
from discord.ext import commands

client = commands.Bot(command_prefix="!")


@client.command(name = "prune", description = "Bulk deletes messages", aliases = ["delete", "bulkdel"], usage = "<number of messages (1-99)>")
async def prune(message):
    if message.memeber.hasPermission("Manage Message"):
        amount = int(message) + 1

        if isnan(amount) or amount < 2 or amount > 100:
            return message.reply("THAts not A vaLId intEGer NIGba. \nGOTa be 1 - 99")

    else:
        await message.channel.send("You DON;t HAVe PERms you WORTHELs PIECE oFGARBAJE")






