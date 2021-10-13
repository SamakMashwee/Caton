from random import randint

with open("commands_caton/variables/the_raven.txt", encoding="utf8") as file:
    verses = file.read().split("\n\n")
    file.close()

async def execute(client, message, args, command, prefix):
    await message.channel.send(f"```{verses[randint(0, len(verses)-1)]}```")