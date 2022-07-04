from pyrogram import Client, filters

Santhu=Client(
    "New bot", 
    "api_id="11318835", 
    "api_hash="945c95cddeb82bf8193a8cabfeb1f958", 
    "bot_token="5511885320:AAEO0OjBCFSMoKmpndNCUEs7PtjYSDYwbdk",
) 


@Santhu.on_message(filters.command("start"))
async def start(bot, message):
    await message.reply_text("👋🏻Hello iam a official pyrogram bot")

@Santhu.on_message(filters.command("help"))
async def help(bot, message):
    await message.reply_text("this is the help for you click the below buttons☺")



Santhu.run() 
