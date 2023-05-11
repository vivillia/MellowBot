import discord
from discord.ext import commands
import json

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def anniversary(ctx):
    await ctx.send('march 28th, 2022')

with open('credentials.json', 'r') as file:
    credentials = json.load(file)

mellowBotToken = credentials["token"]

bot.run(mellowBotToken)