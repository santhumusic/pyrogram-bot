from pyrogram import Client, filters
from pyrogram import Message

Santhu = Client(
    "New bot",
    bot_token="", 
    api_id="", 
    api_hash=""
) 

@Santhu.on_message(filters.command("start"))
async def start(bot, message):
    await message.reply_text("👋🏻Hello iam a official pyrogram bot")

@Santhu.on_message(filters.command("help"))
async def help(bot, message):
    await message.reply_text("this is the help for you click the below buttons☺")



Santhu.run() 
