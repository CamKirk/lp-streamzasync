from flask import Flask, Response, jsonify
import random
import json

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Please use the /data route to receive a datapoint, or use /stream to stream data. "
    })

seed = {
    "open": 24.21,
    "close": 27.85,
    "high": 31.01,
    "low": 22.98,
    "volume": 2298
}

# high must be higher than low
# if high lower than close, set to close

def randOHLCV():

    for key, val in seed.items():
        seed[key] = round(random.gauss(val,0.4), 2)
        if seed[key] < 0: 
            # print("negative", seed[key])
            seed[key] = seed[key]*-1
        seed["volume"] = round(random.gauss(seed["volume"], 1000))
        if seed["volume"] > 1000000:
            seed["volume"]=round(seed["volume"]/1000)
    
    posneg = 0
    if seed["close"] > seed["open"]:
        posneg = 1
    else:
        posneg=-1

    if posneg == 1:
        while seed["high"] < seed["close"] or seed["low"] > seed["open"]:
            seed["high"] = seed["close"]
            seed["low"] = seed["open"]
    if posneg == -1:
        while seed["low"] > seed["close"] or seed["high"] < seed["open"]:
            seed["high"] = seed["open"]
            seed["low"] = seed["close"]
    
    
    return seed

@app.route("/data")
def data():
    return jsonify(randOHLCV())

@app.route("/stream")
def stream():

    def yielder():
        while True:
            yield json.dumps(randOHLCV())+"\n"

    return Response(yielder(), mimetype="text/json")

app.run(host="0.0.0.0")