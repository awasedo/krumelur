from discord.ext import commands
import discord

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group("help")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title = "Command categories", color = self.bot.embed_color,
            description = "These are all currently available command categories")
            embed.add_field(name = ":gear: Configuration", value = "`.help config`")
            embed.add_field(name = ":hammer_pick: Utility", value = "`.help utility`")
            embed.add_field(name = ":laughing: Fun", value = "`.help fun`")
            embed.add_field(name = ":information_source: Information", value = "`.help info`")
            await ctx.send(embed = embed)

    @help.command(name = "utility")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def help_utility(self, ctx):
        utility_embed = discord.Embed(title = "Utility Commands", color = self.bot.embed_color,
        description = "These are all currently available utility commands, use them without the <>")
        utility_embed.add_field(name = "Say", value = "`.say <something>`", inline = False)
        utility_embed.add_field(name = "Clear", value = "`.clear <amount>`", inline = False)
        utility_embed.add_field(name = "Add role", value = "`.addrole <rolename>`", inline = False)
        await ctx.send(embed = utility_embed)

    @help.command(name = "fun")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def help_fun(self, ctx):
        fun_embed = discord.Embed(title = "Fun Commands", color = self.bot.embed_color,
        description = "These are all currently available fun commands, use them without the <>")
        fun_embed.add_field(name = "Random", value = "`.random <number_1> <number_2>`", inline = False)
        await ctx.send(embed = fun_embed)

    @help.command(name = "info")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def help_info(self, ctx):
        info_embed = discord.Embed(title = "Info Commands", color = self.bot.embed_color,
        description = "These are all currently available info commands, use them without the <>")
        info_embed.add_field(name = "Info", value = "`.info`", inline = False)
        info_embed.add_field(name = "Source Code", value = "`.source`", inline = False)
        await ctx.send(embed = info_embed)

    @help.command(name = "owner")
    @commands.is_owner()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def help_owner(self, ctx):
        owner_embed = discord.Embed(title = "Owner Commands", color = self.bot.embed_color,
        description = "These are all currently available owner commands, use them without the <>")
        owner_embed.add_field(name = "Reload", value = "`.reload <cog>`", inline = False)
        await ctx.send(embed = owner_embed)

def setup(bot):
    bot.add_cog(Help(bot))
