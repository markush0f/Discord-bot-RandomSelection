import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from numpy import random

load_dotenv()


token = os.getenv("token")

intents = discord.Intents.all()
intents.messages = True
intents.members = True
bot = commands.Bot(command_prefix="?", intents=intents)
members = []


@bot.event
async def on_ready():
    print(f"Bot conected like {bot.user}")
    for guild in bot.guilds:
        print(f"{guild.name} (ID: {guild.id})")

    guild = bot.guilds[0]

    # for member in guild.members:
    #     print(member)
    global members
    members = [
        member.name for member in guild.members if member.name != "SelecctionRandom"
    ]
    print(members)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "hola" in message.content.lower():
        await message.channel.send(f"Hola {message.author.name}")

    await bot.process_commands(message)


@bot.command()
async def info(context):
    await context.send("Im a bot developed by Markus!!")


@bot.command()
async def select_random(context):
    # print("Members: ", members)
    print("Random: ", members[random.randint(len(members))])
    await context.send("Member random selected: ",members[random.randint(len(members))])

bot.run(token)
