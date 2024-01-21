from os import getenv
from dotenv import load_dotenv

#Necessary Variables 
API_ID = int(getenv("API_ID", 1859341))
API_HASH = getenv("API_HASH", "8d1de558964d482b32b9b65d0e2c5377")
BOT_TOKEN = getenv("6799250953:AAF3WsUC9gFfO_R6USYG42rxzzNCyw_r3nQ") #Put your bot token here
CHANNEL = getenv("CHANNEL", "billabombay") #Your public channel username without @ for force subscription.
MONGO = getenv("mongodb+srv://mathewmaxton:4PLBCZ4xhxlYB7II@cluster0.udnd6vl.mongodb.net/?retryWrites=true&w=majority") #Put mongo db url here
#Optional Variables
OWNER_ID = int(getenv("OWNER_ID", 6542673293)) #Go to @ThunderrXbot and type /id and put that value here. 
FSUB = bool(getenv("FSUB", False)) #Set this True if you want to enable force subscription from users else set to False.
