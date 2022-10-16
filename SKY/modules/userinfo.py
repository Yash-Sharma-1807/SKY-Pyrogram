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

   
from pyrogram.types import Message
from pyrogram import filters
from SKY import app
from pyrogram.enums.parse_mode import ParseMode

@app.on_message(filters.command("info"))
@app.on_edited_message(filters.command('info'))
async def info(_,msg:Message):
    m = await msg.reply_text("Searching...")
    if msg.reply_to_message:
        user = msg.reply_to_message.from_user.id

    elif not msg.reply_to_message and len(msg.command) == 1:
        user = msg.from_user.id
        
    elif not msg.reply_to_message and len(msg.command) != 1:
        user = msg.text.split(None, 1)[1]
        
    x = await app.get_users(user)
    z = """User id : <code>{}</code> \nName : {} \nDC id : <code>{}</code>\nPermanent Link : <a href='tg://user?id={}'>{}</a>""".format(x.id,x.first_name,x.dc_id,x.id,x.first_name)
    file = x.photo.big_file_id if x.photo else None
    photo = await app.download_media(file)
    await m.delete()
    await msg.reply_photo(photo,
        caption=z,parse_mode= ParseMode.HTML)
    
