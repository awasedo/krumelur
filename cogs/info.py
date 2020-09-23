from datetime import datetime
from discord.ext import commands
import discord

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "info")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def info(self, ctx):
        guild_count = len(self.bot.guilds)

        embed = discord.Embed(color = self.bot.embed_color)
        embed.set_thumbnail(url = self.bot.user.avatar_url)
        embed.set_author(name = f"{self.bot.user.name}")
        embed.add_field(name = "Bot Creator:", value = "eschillus#4840", inline = False)
        embed.add_field(name = "Servers:", value = guild_count, inline = False)
        embed.add_field(name = "Bot created:", value = self.bot.user.created_at.strftime("%B %d, %Y"), inline = False)
        await ctx.send(embed = embed)

    @commands.command(name = "sourcecode")
    async def source_code(self, ctx):
        embed = discord.Embed(description = "[Click here!](https://github.com/eschillus/krumelur)", color = self.bot.embed_color)
        embed.set_author(name = "Source code for the Krumelur bot!",
        icon_url = self.bot.user.avatar_url)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Info(bot))
