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
from SKY import app, uptime
from pyrogram import filters
from pyrogram.types import Message

@app.on_message(filters.command("ping"))
@app.on_edited_message(filters.command("ping"))
async def ping(_,msg:Message):
    start_time = datetime.datetime.now()
    x = await msg.reply_text("Pong..")
    end_time = datetime.datetime.now()
    tgping = (end_time - start_time).microseconds / 1000
    upt = datetime.datetime.utcnow()
    await x.edit_text("Current Ping : `{}` ms\nCurrent Uptime : `{}`".format(tgping,uptime(upt)))