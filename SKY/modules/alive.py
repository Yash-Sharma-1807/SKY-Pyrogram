from re import L
from SKY import app
from pyrogram import filters
from pyrogram.types import Message

Alive_ani = "https://telegra.ph/file/b21a418fa01eb8b313804.mp4"

@app.on_command(filters.command("alive"))
async def alive(_,msg:Message):
    await msg.reply_animation(Alive_ani,caption="Well Hello There I am alive")
