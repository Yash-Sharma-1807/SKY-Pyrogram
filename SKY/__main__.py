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

import importlib
import sys
from pyrogram import idle
import asyncio
from SKY import app
from SKY.module import z
sys.dont_write_bytecode=True

loop = asyncio.get_event_loop()

async def main():
    global HELPABLE
    print("Starting BOT")
    

    try :
        
        for all_mods in z:
            x = importlib.import_module("SKY.module" + all_mods)
        print("Sucessfully loaded all modules"+str(x))
        await app.send_message(-1001623932405, text = "Hello There Bitches")
        print("BOT Started Sucessfully")
    except :
        print("App Didn't Start")

if __name__ == "__main__":
    loop.run_until_complete(main())

