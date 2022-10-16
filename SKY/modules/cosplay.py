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
from pyrogram import filters
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup
from SKY import app
import requests

@app.on_message(filters.command("cosplay"))
async def cosplay(_,msg:Message):
    img = requests.get("https://waifu-api.vercel.app").json()
    await msg.reply_photo(img)

@app.on_message(filters.command("ncosplay") & filters.group)
async def no(_,msg:Message):
    await msg.reply_text("Sorry you can use this command only in private chat with bot",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Click Here",url=f"https://t.me/SKYXRobot?start=")]
            ]
        ))

@app.on_message(filters.command("ncosplay") & filters.private)
async def cosplay(_,msg:Message):
    ncosplay = requests.get("https://waifu-api.vercel.app/items/1").json()
    await msg.reply_photo(ncosplay)
