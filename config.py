# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "15236804"))
API_HASH = os.environ.get("API_HASH", "409da5b68ad699091fa72b381921f0e5")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6234844092:AAFBOasCCD-KFuwgspTKsJr_fyZuzPtnNcI")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1963114305")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Converter")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Matin:SMwBGa029I2bs5Vv@cluster0.ygefm.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1963114305")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(1963114305)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001684353224")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "MPlayLink") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
