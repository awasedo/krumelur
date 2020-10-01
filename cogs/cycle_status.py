import asyncio
from random import choice

import discord
from discord.ext import commands, tasks


class CycleStatus(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.cycle_status.start()

    @tasks.loop(minutes=3)
    async def cycle_status(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            self.bot.statuses = ["", "", ""]
            status = discord.Activity(type=discord.ActivityType.streaming,
                                      url="https://www.twitch.tv/krumelur-discord-bot",
                                      name=f"{choice(self.bot.statuses)} ?help")
            await self.bot.change_presence(activity=status)
            await asyncio.sleep(60)


def setup(bot):
    bot.add_cog(CycleStatus(bot))
