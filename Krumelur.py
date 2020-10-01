import json

from discord.ext.commands import Bot

from utils.format import info
import discord
import json

with open('data/config.json', 'r') as c:
    config = json.load(c)


class Krumelur(Bot):
    def __init__(self):
        super().__init__(command_prefix=config["bot_prefix"], owner_id=config["owner_id"])

        self.remove_command("help")
        self.embed_color = 0xff8800
        self.embed_error_color = 0xf81212
        self.embed_good_color = 0x12f82c

        for cog in config["cogs"]:
            self.load_extension(f"cogs.{cog}")
            info(f"Loaded {cog}!")


Krumelur().run(config["bot_token"])
