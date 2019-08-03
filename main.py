from db import session
from db.models import Ticker
import ccxt 
import time
import datetime

exchange = ccxt.okcoinusd()
exchange.load_markets()

if exchange.has['fetchOHLCV']:
    for symbol in exchange.markets:
        time.sleep (exchange.rateLimit / 1000) # time.sleep wants seconds
        ohlcvs = exchange.fetch_ohlcv(symbol, '1d')
        print(len(ohlcvs))
        for data in ohlcvs:
            d, o, h, l, c, v = data
            # print(d)
            d = datetime.datetime.fromtimestamp(d/1000)
            t = Ticker(symbol=symbol, timestamp=d, open=o, high=h, low=l, close=c, volume=v)
            session.add(t)
        session.commit()

