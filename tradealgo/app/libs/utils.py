from datetime import datetime
import pandas as pd

def ts():
    return pd.Timestamp.now()

def log(*args, **kwargs):
    print(ts(), " ", *args, **kwargs)

def ms2date(ms, fmt="%Y-%m-%d"):
    if isinstance(ms, pd.Timestamp):
        return ms.strftime(fmt)
    else:
        return datetime.fromtimestamp(ms/1000).strftime(fmt)