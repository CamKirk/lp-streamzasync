import pprint
import asyncio
import pandas as pd
from datetime import datetime
from alpaca_trade_api import StreamConn
import logging

opt = None

def ts():
    return pd.Timestamp.now()

def log(*args, **kwargs):
    print(ts(), " ", *args, **kwargs)

def debug(*args, **kwargs):
    print(ts(), " ", **kwargs)

def ms2date(ms, fmt="%Y-%m-%d"):
    if isinstance(ms, pd.Timestamp):
        return ms.strftime(fmt)
    else:
        return datetime.fromtimestamp(ms/1000).strftime(fmt)

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
    {channel:<6s} {ms2date(bar.end)} {bar.symbol:<10s}
    {percent:>8.2f}% {bar.open:>8.2f} {bar.close:>8.2f}
    {bar.volume:<10d}
    """)

async def on_data(conn, channel, data):
    if opt or not (channel in ("AM", "Q", "A", "T")):
        debug("debug: ", pprint.pformat(data))

async def on_tick(conn, channel, bar):
    try:
        percent = (bar.close - bar.dailyopen)/bar.close*100
    except:
        percent = 0

    print(f"""
    {channel:<6s} {ms2date(bar.end)} {bar.symbol:<10s}
    {percent:>8.2f}% {bar.open:>8.2f} {bar.close:>8.2f}
    {bar.volume:<10d}
    """)
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)


    # conn and assignment to handlers
    # TODO: move to the decorator function style
    conn = StreamConn()

    on_minute = conn.on(r"AM$")(on_minute)
    on_tick = conn.on(r'A$')(on_tick)
    on_data = conn.on(r".*")(on_data)

    try:
        conn.run(["Q.*","T.*","AM.*","A.*"])
    # else:
    #     conn.run(["AM.*"])
    except Exception as e:
        print(e)