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
from pyrogram import Client
from SKY.config import Config

ID = Config.API_ID
HASH = Config.API_HASH
TK = Config.BOT_TOKEN
SUPPORT = Config.Support
OWNER = Config.OWNER_ID



app = Client("SKY",api_id= ID, api_hash= HASH, bot_token= TK)

print("Starting APP")
app.start()

c = app.get_me()
BOT_ID = c.id
BOT_NAME = c.first_name 
BOT_USERNAME = c.username

now = datetime.datetime.utcnow()

def uptime(self):
        delta = self - now
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        if days:
            fmt = '{d} days, {h} hours, {m} minutes, and {s} seconds'
        else:
            fmt = '{h} hours, {m} minutes, and {s} seconds'

        return fmt.format(d=days, h=hours, m=minutes, s=seconds) 