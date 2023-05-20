import os

class Config(object):
    BANNED_USERS = []
    DOWNLOAD_LOCATION = "./DOWNLOADS" 
    API_ID = int(os.environ.get("API_ID", "24079851")
    API_HASH = os.environ.get("API_HASH" "a4eee8cd21bf557b7a75840e8d6ef6df")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5993298723:AAHcYVVW9zWpd5XbtQchvFcuUM6kqmhzPj0")
    OWNER_ID = int(os.environ.get("OWNER_ID", "Raj4339"))
    AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", "1001958947052")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Rajbot:Rajbot@cluster0.ifgyoay.mongodb.net/?retryWrites=true&w=majority")
