
from pyrogram import filters
from pyrogram.types import Message
from SKY import app
import requests

@app.on_message(filters.command("cosplay"))
async def cosplay(_,msg:Message):
    img = requests.get("https://waifu-api.vercel.app").json()
    await msg.reply_photo(img)


@app.on_message(filters.command("ncosplay"))
async def cosplay(_,msg:Message):
    ncosplay = requests.get("https://waifu-api.vercel.app/items/1").json()
    await msg.reply_photo(ncosplay)
