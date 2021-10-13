from random import randint

riddles = []

with open("commands_caton/variables/riddles_and_answers.txt") as file:
	data = file.readlines()
	file.close()

for counter in range(len(data)):
	if counter % 2 == 0:
		riddles.append([data[counter]])
		riddles[int(counter/2)].append(data[counter+1])

riddle_count = len(riddles)

async def execute(client, message, args, command, prefix):
	riddle_index = randint(0, riddle_count-1)
	await message.channel.send(f"{riddles[riddle_index][0]}\n||{riddles[riddle_index][1]}||")