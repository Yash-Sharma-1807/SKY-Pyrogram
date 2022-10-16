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

   
from SKY import app, BOT_ID
from pyrogram import enums, filters
from pyrogram.types import Message
import asyncio

# GET ADMINS

@app.on_message(filters.private & filters.command("getadmins"))
async def get(_,msg:Message):
    await msg.reply_text("This Doesn't Work in pm")

# BAN

@app.on_message(filters.group & filters.command("getadmins"))
async def getadmins(_,msg:Message):
    m = await msg.reply_text("Getting Admins And Bots....")
    AD = "ADMINS :-"
    BT = "\n\nBOTS :-"
    async for x in app.get_chat_members(msg.chat.id,filter= enums.ChatMembersFilter.ADMINISTRATORS):
        try:
            AD += "\n[{}](tg://user?id={})".format(x.user.first_name,x.user.id)
        except Exception as e:
            await m.edit_text(e)
    async for y in app.get_chat_members(msg.chat.id,filter=enums.ChatMembersFilter.BOTS):
        try:
            BT += "\n[{}](tg://user?id={})".format(y.user.first_name,y.user.id)
        except Exception as e:
            await m.edit_text(e)
    await m.delete()
    ALL = AD + BT
    await msg.reply_text(ALL)

# UNBAN

@app.on_message(filters.group & filters.command("ban"))
async def ban(_,msg:Message):
    ad = await app.get_chat_member(msg.chat.id,msg.from_user.id)
    
    if not msg.reply_to_message:
        await msg.reply_text("Tag someone")
    
    elif msg.reply_to_message.from_user.id == BOT_ID :
        await msg.reply_text("Bro next time you do this you will get banned")

    elif msg.from_user.id == msg.reply_to_message.from_user.id :
        await msg.reply_text("Want to BAN yourself ?")


    elif msg.from_user.id != msg.reply_to_message.from_user.id :
        try:
            if ad.privileges.can_restrict_members == True : 
                x = await msg.reply_text("👍")
                await asyncio.sleep(0.5)
                await x.edit_caption("Banning This person")
                await app.ban_chat_member(msg.chat.id,msg.reply_to_message.from_user.id)
                await x.edit_caption("Sucessfully banned {}".format(msg.reply_to_message.from_user.first_name))
        except :
            await msg.reply_text("You lack permissions")


@app.on_message(filters.group & filters.command("unban"))
async def unban(_,msg:Message):
    ad = await app.get_chat_member(msg.chat.id,msg.from_user.id)
    
    if not msg.reply_to_message:
        await msg.reply_text("Tag someone")
    
    elif msg.reply_to_message.from_user.id == BOT_ID :
        await msg.reply_text("I am already here")

    elif msg.from_user.id == msg.reply_to_message.from_user.id :
        await msg.reply_text("Want to Unban yourself ?")


    elif msg.from_user.id != msg.reply_to_message.from_user.id :
        try:
            if ad.privileges.can_restrict_members == True : 
                x = await msg.reply_text("Unbanning This person")
                await app.unban_chat_member(msg.chat.id,msg.reply_to_message.from_user.id)
                await asyncio.sleep(0.5)
                x.edit_caption("Sucessfully unbanned {}".format(msg.reply_to_message.from_user.first_name))

        except :
            await msg.reply_text("You lack permissions")