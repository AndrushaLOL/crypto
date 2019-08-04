from db import session
from db.models import Ticker
import ccxt.async_support as ccxt
import asyncio
import time
import datetime

exchange = ccxt.okcoinusd()
ioloop = asyncio.get_event_loop()

async def main():
    await exchange.load_markets()

async def get_ohlcv(exchange, symbol):
    # await time.sleep(exchange.rateLimit/1000)
    ohlcvs = await exchange.fetch_ohlcv(symbol, '1h')
    print(len(ohlcvs))
    for data in ohlcvs:
        d, o, h, l, c, v = data
        d = datetime.datetime.fromtimestamp(d/1000)
        # print(d)
        t = Ticker(symbol=symbol, timestamp=d, open=o, high=h, low=l, close=c, volume=v)
        session.add(t)
    session.commit()
    await exchange.close()

if exchange.has['fetchOHLCV']:
    tasks = [main()]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)

    tasks =  [ioloop.create_task(get_ohlcv(exchange, symbol)) for symbol in exchange.markets]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)
    ioloop.close()
