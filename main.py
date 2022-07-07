from pyrogram import Client, filters
from pyrogram import Message
from config import BOT_TOKEN, API_ID, API_HASH
Santhu = Client(
    "New bot",
    bot_token=BOT_TOKEN, 
    api_id=API_ID, 
    api_hash=API_HASH
) 

@Santhu.on_message(filters.command("start"))
async def start(bot, message):
    await message.reply_text("👋🏻Hello iam a official pyrogram bot")

@Santhu.on_message(filters.command("help"))
async def help(bot, message):
    await message.reply_text("this is the help for you click the below buttons☺")



Santhu.run() 
