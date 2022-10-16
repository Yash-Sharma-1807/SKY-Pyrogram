"""
Copyright (c) 2022 Yash-Sharma-1807

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
   """



import datetime
import importlib
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import asyncio
from SKY import SUPPORT, app, uptime, BOT_NAME, BOT_USERNAME 
from SKY.modules import x
from pyrogram.enums.parse_mode import ParseMode
loop = asyncio.get_event_loop()

async def start_bot():
    global HELPABLE

    for module in x:
        imported_module = importlib.import_module("SKY.modules." + module)
        if (
                hasattr(imported_module, "__MODULE__")
                and imported_module.__MODULE__
        ):
            imported_module.__MODULE__ = imported_module.__MODULE__
            if (
                    hasattr(imported_module, "__HELP__")
                    and imported_module.__HELP__
            ):
                HELPABLE[
                    imported_module.__MODULE__.replace(" ", "_").lower()
                ] = imported_module
    bot_modules = ""
    j = 1
    for i in x:
        if j == 4:
            bot_modules += "|{:<15}|\n".format(i)
            j = 0
        else:
            bot_modules += "|{:<15}".format(i)
        j += 1
    print("Loaded these Modules")
    print(bot_modules)
    await app.send_animation(SUPPORT,"https://telegra.ph/file/c8e5d670ff91438779a5e.mp4",
        caption="{} has Started".format(BOT_NAME))
    await idle()
    




@app.on_message(filters.command("start") & filters.group)
async def start(_,msg):
    Alive_time = datetime.datetime.utcnow()
    await msg.reply_text("I am Alive \n\nAlive Since : <code>{}</code>".format(uptime(Alive_time)),parse_mode= ParseMode.HTML)
    
@app.on_message(filters.command("start") & filters.private)
async def start(_,msg:Message):
    Alive_time = datetime.datetime.utcnow()
    await msg.reply_text("Hello There I am {} \nAlive Since : {}".format(BOT_NAME,uptime(Alive_time)),
        reply_markup= InlineKeyboardMarkup(
            [
                    [InlineKeyboardButton("Add Me To Your Group",url= "https://t.me/SKYXRobot?startgroup=true"),]
            ]))

if __name__ == "__main__":
    loop.run_until_complete(start_bot())

