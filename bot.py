# SuzeBot
# Copyright (C) 2026 kurisuisbestgirl

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import discord
from discord.ext import commands

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
