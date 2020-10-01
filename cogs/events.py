import os

import discord
from discord.ext import commands

from utils.format import info


class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        os.system("clear")
        info("Logging in...")

    @commands.Cog.listener()
    async def on_ready(self):
        os.system("clear")
        info(f"Logged in as: {self.bot.user}")
        info(f"Using discord.py {discord.__version__}")
        info(f"Connected to {len(self.bot.guilds)} servers!")


def setup(bot):
    bot.add_cog(Events(bot))
