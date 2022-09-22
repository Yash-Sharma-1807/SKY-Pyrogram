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
from pyrogram import idle
import asyncio
from SKY import app
from SKY.modules import x

loop = asyncio.get_event_loop()


async def start_bot():
    global HELPABLE

    for module in x:
        imported_module = importlib.import_module("SKY.modules." + module)
        if (
                hasattr(imported_module, "__MODULE__")
                and imported_module.__MODULE__
        ):
            imported_module.__MODULE__ = imported_module.__MODULE__
            if (
                    hasattr(imported_module, "__HELP__")
                    and imported_module.__HELP__
            ):
                HELPABLE[
                    imported_module.__MODULE__.replace(" ", "_").lower()
                ] = imported_module
    bot_modules = ""
    j = 1
    for i in x:
        if j == 4:
            bot_modules += "|{:<15}|\n".format(i)
            j = 0
        else:
            bot_modules += "|{:<15}".format(i)
        j += 1
    print("Loaded these Modules")
    print(bot_modules)
    await app.send_animation(-1001623932405,"https://telegra.ph/file/113a6d5ad54a20917e4df.mp4",caption="I am Alive")
    await idle()
    

if __name__ == "__main__":
    loop.run_until_complete(start_bot())

