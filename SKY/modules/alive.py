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

from SKY import app
from pyrogram import filters
from pyrogram.types import Message

Alive_ani = "https://telegra.ph/file/b21a418fa01eb8b313804.mp4"

@app.on_message(filters.command("alive",prefixes="/"))
async def alive(_,msg:Message):
    await msg.reply_animation(Alive_ani,caption="Well Hello There I am alive")
