import os

API_ID = API_ID =29485859

API_HASH = os.environ.get("API_HASH", "6628abb836f1ab2eaca4df8c514d291a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6896373704:AAH4O4Sn97B9I8qX-p9ReTfQQI7aBDbSbmI")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6045786693))

LOG = -1002140760823

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5987970971").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


