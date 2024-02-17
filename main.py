import os
from pyrogram import Client
from config import Config

Bot = Client(
    "Simple Bot",
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH,
    plugins = dict(root="plugins")
)


Bot.run()
