from discord.ext.commands import Bot
from utils.format import info
import discord
import json

with open("utils/config.json", "r") as c:
    config = json.load(c)

class Krumelur(Bot):
    def __init__(self):
        super().__init__(command_prefix=config["krumelur_prefix"], owner_id=config["owner_id"])

        self.remove_command("help")
        self.embed_color = 0xff8800
        self.embed_error_color = 0xf81212
        self.embed_good_color = 0x12f82c

        for extension in config["extensions"]:
            self.load_extension(f"cogs.{extension}")
            info(f"Loaded {extension}!")

Krumelur().run(config["krumelur_token"])
