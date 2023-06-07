import discord
from discord.ext import commands
import json
import gspread
from dotenv import load_dotenv
import os

env_vars = load_dotenv('.env')

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key("18y3BVsmo65efd4qFI4FkM9WgW0TFep4mMD7ExsB9Q1E")
#setting up google spreadsheet

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def anniversary(ctx):
    await ctx.send('march 28th, 2022')

@bot.command()
async def ImportantDates(ctx):
    await ctx.send('march 28th, 2022')

with open('credentials.json', 'r') as file:
    credentials = json.load(file)

mellowBotToken = os.environ.get('token')

bot.run(mellowBotToken)