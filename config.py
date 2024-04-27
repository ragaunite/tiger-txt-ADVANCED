import os

API_ID = API_ID = 5169536

API_HASH = os.environ.get("API_HASH", "2661fc89c0040bf336947a9d392532f4")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7013028296:AAEhG6gEZDOU9Xwnv8444xP2ALL0nzAZf20")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6725604714))

LOG = -1002010655950

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5987970971").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


