import websockets
import asyncio 
import json
import uuid
url = 'https://dpdpwl.tistory.com/'
# print(uuid.uuid1())
async def upbit_ws_client():
    uri = "wss://api.upbit.com/websocket/v1"

    async with websockets.connect(uri) as websocket:
        subscribe_fmt = [ 
            {"ticket":str(uuid.uuid4())}, # 식별값 유니크한 값
            {
                "type": "ticker", # ticker -> 현재가, trade -> 체결, orderbook => 호가
                "codes":["KRW-BTC", "KRW-ETH"], # 수신 시세 종목 정보 (대문자)
                "isOnlyRealtime": True # 실시간 시세만
            },
            {"format":"SIMPLE"} # simple -> 간소화,
        ]
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)

        while True:
            data = await websocket.recv()
            data = json.loads(data)
            print(data)


async def main():
    await upbit_ws_client()

asyncio.run(main())