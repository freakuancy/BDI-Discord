# BDI-Wiki.py, a Discord port of the Eggdrop TCL script
# Takes a basic search term and integrates it into a wiki link
# 2020 freakuancy@gmail.com

# dependancies
import os
import random
from dotenv import load_dotenv
from discord.ext import commands

# securely load bot token from userenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# create new bot object
bot = commands.Bot(command_prefix='!')

# on connect
@bot.event
async def on_ready():
	print(f'{bot.user} has connected to Discord!')

# on command
@bot.command(name='wiki', help='Displays a helpful link to a specified BDI wiki subject')

async def wikilink(ctx, *article):
	out = ' '
	# Avoid recursive trigger
	if ctx.author == bot.user:
		return
	# Compose link in BDI MediaWiki format
	for word in article:
		if word == 'of' or word == 'the' or word == 'if' or word == 'and' or word == 'is' or word == 'a':
         		s = word
		else:
	 		s = word[0].upper() + word[1:]
		out = out + ' ' + s
	complete = out.strip().replace(' ', '_')
	# Fill in empty request
	if complete == '':
		complete = 'Main_Page'
	# Send composed link to server
	await ctx.send('http://www.blkdragon.com/wiki/index.php?title=' + complete)

# begin run loop
bot.run(TOKEN)
