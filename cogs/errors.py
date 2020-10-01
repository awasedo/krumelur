import discord
from discord.ext import commands


class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, "on_error"):
            ctx.command = command
            return

        error = getattr(error, "original", error)

        if isinstance(error, commands.NoPrivateMessage):
            embed = discord.Embed(title="This command can not be used here!", color=self.bot.embed_error_color)
            await ctx.send(embed=embed)

        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="This command requires an argument!", color=self.bot.embed_error_color)
            await ctx.send(embed=embed)

        elif isinstance(error, commands.NotOwner):
            embed = discord.Embed(title=f"You are not the owner of this bot!", color=self.bot.embed_error_color)
            await ctx.send(embed=embed)

        elif isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title=f"{error}", color=self.bot.embed_error_color)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Errors(bot))
