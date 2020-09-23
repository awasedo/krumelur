import discord
from aiohttp import ClientSession
from discord.ext import commands
from random import randint

class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name = "randint", aliases = ["random"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def randint(self, ctx, number_1: int, number_2: int):
        randomnumber = randint(number_1, number_2)
        await ctx.send(randomnumber)

def setup(bot):
    bot.add_cog(Fun(bot))
