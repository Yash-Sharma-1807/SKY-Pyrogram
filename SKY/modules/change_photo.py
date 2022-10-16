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


import asyncio
from SKY import app
from pyrogram.types import Message
from pyrogram import filters

DOWNLOAD_LOCATION = "./DOWNLOADS/okh.jpg"


@app.on_message(filters.command("setgpic"))
async def setpfp(_,msg:Message):
    cc = await app.get_chat_member(msg.chat.id,msg.from_user.id)
    if cc.privileges.can_change_info == True:
        if not msg.reply_to_message:
            await msg.reply_text("Tag a image Pro")
        else:
            y = await app.send_message(chat_id= msg.chat.id, reply_to_message_id= msg.reply_to_message_id, text= "Setting this image as new chat pfp")
            await app.set_chat_photo(chat_id = msg.chat.id,photo=DOWNLOAD_LOCATION)
            await asyncio.sleep(2)
            await y.delete()
            await app.send_message(chat_id= msg.chat.id, reply_to_message_id= msg.reply_to_message_id,text= "Sucessfully setted this as new chat pfp")

    else :
        await msg.reply_text("U lack permissions kid")