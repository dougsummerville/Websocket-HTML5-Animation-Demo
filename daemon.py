import asyncio
from websockets import serve

async def rx_hndlr(websocket):
    try:
        async for message in websocket:
            print(message)
    except: 
        pass
async def tx_hndlr(websocket):
    try:
        i=0;
        while True:
            i=i+1
            await websocket.send("%d"%(i))
            await asyncio.sleep(1)
    except:
        pass

async def msg_handler(websocket, path):
    await asyncio.gather(
            rx_hndlr(websocket),
            tx_hndlr(websocket))
async def main():
    await asyncio.gather(
            mainwebinterface(),
            mainprojectorloop())

async def mainwebinterface():
    print("starting web interface()")
    while True:
        print("hello")
        await asyncio.sleep(1)

async def mainprojectorloop():
    print("starting mainloop()")
    async with serve( msg_handler, "localhost", 10001 ):
        await asyncio.Future()

print("Starting projector daemon")
asyncio.run(main())
