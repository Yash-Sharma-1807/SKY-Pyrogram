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
   
from pyrogram import Client
from SKY.config import Config

ID = Config.API_ID
HASH = Config.API_HASH
TK = Config.BOT_TOKEN



app = Client("SKY",api_id= ID, api_hash= HASH, bot_token= TK)

print("Starting APP")
app.start()