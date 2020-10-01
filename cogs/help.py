import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="help", aliases=["h", "krumelur", "bot"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(
                title="Command categories",
                color=self.bot.embed_color,
                description="These are all currently available command categories"
            )
            embed.add_field(name=":gear: Configuration",
                            value=f"`{self.bot.command_prefix}help config`")
            embed.add_field(name=":hammer_pick: Utility",
                            value=f"`{self.bot.command_prefix}help utility`")
            embed.add_field(name=":laughing: Fun",
                            value=f"`{self.bot.command_prefix}help fun`")
            embed.add_field(name=":information_source: Information",
                            value=f"`{self.bot.command_prefix}help info`")
            await ctx.send(embed=embed)

    @help.group(name="utility")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def help_utility(self, ctx):
        if ctx.invoked_subcommand is None:
            utility_embed = discord.Embed(
                title="Utility Commands", color=self.bot.embed_color,
                description="These are all currently available utility commands, use them without the <>"
            )
            utility_embed.add_field(name="Say",
                                    value=f"`{self.bot.command_prefix}say <something>`", inline=False)
            utility_embed.add_field(name="Clear",
                                    value=f"`{self.bot.command_prefix}clear <amount>`", inline=False)
            utility_embed.add_field(name="Add role",
                                    value=f"`{self.bot.command_prefix}addrole <rolename>`", inline=False)
            await ctx.send(embed=utility_embed)

    @utility.command(name="say")
    async def help_utility_say(self, ctx):
        utility_say_embed = discord.Embed(
            title="Say Command", color=self.bot.embed_color,
            description=f"This is the say command"
        )

    @utility.command(name="clear")
    async def help_utility_clear(self, ctx):
        utility_say_embed = discord.Embed(
            title="Clear Command", color=self.bot.embed_color,
            description=f"This is the clear command"
        )

    @utility.command(name="addrole")
    async def help_utility_addrole(self, ctx):
        utility_say_embed = discord.Embed(
            title="Addrole Command", color=self.bot.embed_color,
            description=f"This is the addrole command"
        )

    @help.command(name="fun")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def help_fun(self, ctx):
        fun_embed = discord.Embed(
            title="Fun Commands", color=self.bot.embed_color,
            description="These are all currently available fun commands, use them without the <>"
        )
        fun_embed.add_field(name="Random",
                            value=f"`{self.bot.command_prefix}random <number_1> <number_2>`", inline=False)
        await ctx.send(embed=fun_embed)

    @help.command(name="info")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def help_info(self, ctx):
        info_embed = discord.Embed(
            title="Info Commands", color=self.bot.embed_color,
            description="These are all currently available info commands, use them without the <>"
        )
        info_embed.add_field(name="Info",
                             value=f"`{self.bot.command_prefix}info`", inline=False)
        info_embed.add_field(name="Source Code",
                             value=f"`{self.bot.command_prefix}sourcecode`", inline=False)
        await ctx.send(embed=info_embed)

    @help.command(name="owner")
    @commands.is_owner()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def help_owner(self, ctx):
        owner_embed = discord.Embed(
            title="Owner Commands", color=self.bot.embed_color,
            description="These are all currently available owner commands, use them without the <>"
        )
        owner_embed.add_field(name="Reload",
                              value=f"`{self.bot.command_prefix}reload <cog>`", inline=False)
        await ctx.send(embed=owner_embed)


def setup(bot):
    bot.add_cog(Help(bot))
