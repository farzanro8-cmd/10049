from flask import Flask, jsonify
import time
import threading
import random

app = Flask(__name__)

data = {
    "counter": 0,
    "value": 0
}

def generator():
    while True:
        data["counter"] += 1
        data["value"] = random.randint(1, 100)
        time.sleep(1)

@app.route("/")
def home():
    return jsonify(data)

if __name__ == "__main__":
    threading.Thread(target=generator, daemon=True).start()
    app.run(host="0.0.0.0", port=10000)
