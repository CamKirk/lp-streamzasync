from flask import Flask, Response
import random
import json

app = Flask(__name__)

@app.route("/data")
def data_route():
    
    def numbers():
        while True :
            rand = random.randint(1,100)
            yield json.dumps({"value":rand})+"\n" 
            # when using infinite while-loop, have to explicitly add a newline character for the requests' r.iter_lines() to correctly chunk the data.
            # alternatively, could use a static for-loop to stream data.
             

    print(numbers())
    return Response(numbers(), mimetype="text/json")

app.run(debug=True)