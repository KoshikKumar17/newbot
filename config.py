import os
# Bot information
class Config(object):
  APP_ID = int(os.environ.get("APP_ID", ""))
  API_HASH = os.environ.get("API_HASH", "")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  OWNER_ID = 1162032262
