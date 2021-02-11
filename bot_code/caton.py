import discord
from importlib import import_module
from glob import glob
from json import load

# commands need to be in the commands_caton folder for them to be     -#
#- registered in the dict.                                             #
COMMANDS = {filename.replace(".py", "").replace("commands_caton\\", "") : import_module(filename.replace(".py", "").replace("\\", "."))
			for filename in glob("commands_caton/*.py")}

# having the token and the prefix contained in a .json file is ripped -#
#- from discord.js documentation and tutorials.                        #
with open("info.json") as info:
	data = load(info)
	TOKEN = data["token"]
	PREFIX = data["prefix"]
	info.close()

class my_client(discord.Client):

	async def on_ready(self):
		print(f"Logged in as: {self.user.name}{self.user.id}.")
	
	# discord.py tutorials don't use the on_message function to handle commands -#
	#- but the fact that you can't scan every message doesn't allow for proper  -#
	#- file structured programming. so this is why this on_message function is  -#
	#- the command handler for the bot.                                          #
	async def on_message(self, message):

		if message.content.startswith(PREFIX):
			command = message.content.strip(PREFIX)

			try:
				await COMMANDS[command].execute(message)

			except KeyError:
				print("Command does not exist.")
				return

client = my_client()
client.run(TOKEN)