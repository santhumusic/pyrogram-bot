from pyrogram import Client, filters

Santhu=Client(
    "New bot", 
    "api_id="your api id", 
    "api_hash="your api hash here", 
    "bot_token="your bot token",
) 


@Santhu.on_message(filters.command("start"))
async def start(bot, message):
    await message.reply_text("👋🏻Hello iam a official pyrogram bot")

@Santhu.on_message(filters.command("help"))
async def help(bot, message):
    await message.reply_text("this is the help for you click the below buttons☺")
