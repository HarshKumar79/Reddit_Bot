import os
from dotenv import load_dotenv

load_dotenv()

reddit_credentials = {
    "CLIENT_ID": os.getenv("CLIENT_ID"),
    "CLIENT_SECRET": os.getenv("CLIENT_SECRET"),
    "USERNAME": os.getenv("USERNAME"),
    "PASSWORD": os.getenv("PASSWORD"),
    "USER_AGENT": os.getenv("USER_AGENT", "ProductionBot")
}