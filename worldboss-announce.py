# worldboss-announce.py
# Reminder to check for world boss spawns every hour
# For Nova@Old Blanchy
# 2020 github.com/freakuancy

import discord
import asyncio
import os

from dotenv import load_dotenv

# securely load client token from userenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# client object
class MyClient(discord.Client):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# create background task
		self.bg_task = self.loop.create_task(self.my_background_task())
	# on connect
	async def on_ready(self):
		print('Connected to Discord!')
	# background task implementation
	async def my_background_task(self):
		await self.wait_until_ready()
		channel = self.get_channel(702489193674440775)
		while not self.is_closed():
			await channel.send('@here Please remember to check for world event spawns!')
			await asyncio.sleep(3600)

client = MyClient()
# run
client.run(TOKEN)
