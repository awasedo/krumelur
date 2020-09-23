from discord.ext import commands
from discord.utils import get
from random import randint
import discord

class Utility(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name = "embed")
    @commands.has_permissions(manage_messages = True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def embed(self, ctx, *, message):
        embed = discord.Embed(title = message, color = self.bot.embed_color)
        await ctx.channel.send(embed = embed)

    @commands.command(name = "say")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.has_permissions(manage_messages = True)
    async def say(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command(name = "clear", aliases = ["purge", "delete"])
    @commands.has_permissions(manage_messages = True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def clear(self, ctx, limit: int):
        await ctx.channel.purge(limit = limit + 1)

        embed = discord.Embed(title = f"Deleted {limit} messages for you!", color = self.bot.embed_color)
        await ctx.send(embed = embed, delete_after = 3)

    @commands.command(name = "addrole")
    @commands.has_permissions(administrator = True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def addrole(self, ctx, role: str):
        await ctx.guild.create_role(name = role)

        embed = discord.Embed(color = self.bot.embed_color)
        embed.set_author(name = f"Succesfully created the {role} role!")
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Utility(bot))
