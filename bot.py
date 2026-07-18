import discord
from discord.ext import commands
import os

TOKEN = ""

intents = discord.Intents.default()
intents.message_content = True  # THIS is required for reading !commands
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command(name="SuzeNyan~☆")
async def suzenyan(ctx):
    await ctx.send("Nyan!~☆")

bot.run(TOKEN)
