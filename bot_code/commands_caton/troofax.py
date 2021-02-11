from random import randint

with open("../bot_code/commands_caton/variables/troofax.txt") as facts:
    fact_list = facts.readlines()
    facts.close()

async def execute(message):
        await message.channel.send(fact_list[randint(0, len(fact_list)-1)])
        print(fact_list)