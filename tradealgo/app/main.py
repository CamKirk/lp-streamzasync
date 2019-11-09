import pprint
import asyncio
import pandas as pd
from datetime import datetime
from alpaca_trade_api import StreamConn
import logging
from libs import utils, models, db

print(utils)
conn = StreamConn()

@conn.on(r"AM$")
async def on_minute(conn, channel, bar): # bar object is the OHLC
    print(bar)
    
    symbol=bar.symbol
    close=bar.close

    try:
        percent= (close - bar.dailyopen)/close * 100  
        up = 1 if bar.open > bar.dailyopen else -1
    except:
        percent = 0
        up = 0
    
    print(f"""
    {channel:<6s} {utils.ms2date(bar.end)} {bar.symbol:<10s}
    {percent:>8.2f}% {bar.open:>8.2f} {bar.close:>8.2f}
    {bar.volume:<10d}
    """)


@conn.on(r'A$')
async def on_tick(conn, channel, bar):
    try:
        percent = (bar.close - bar.dailyopen)/bar.close*100
    except:
        percent = 0

    print(f"""
    {channel:<6s} {utils.ms2date(bar.end)} {bar.symbol:<10s}
    {percent:>8.2f}% {bar.open:>8.2f} {bar.close:>8.2f}
    {bar.volume:<10d}
    """)
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    try:
        conn.run(["Q.*","T.*","AM.*","A.*"])
    # else:
    #     conn.run(["AM.*"])
    except Exception as e:
        print(e)