
import asyncio
from SKY import app


async def main():
    try :
        await app.start()
        await app.send_message(-1001623932405, text = "Hello There Bitches")
        print("App Started Sucessfully")
    except :
        print("App Didn't Start")

if __name__ == "__main__":
    asyncio.run(main())

