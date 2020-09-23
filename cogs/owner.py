from discord.ext import commands
import discord

class Owner(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name = "reload")
    @commands.is_owner()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def reload(self, ctx, *, cog: str):
        try:
            self.bot.reload_extension("cogs." + cog)
        except Exception as e:
            await ctx.message.add_reaction("❌")
        else:
            await ctx.message.add_reaction("✅")

def setup(bot):
    bot.add_cog(Owner(bot))
