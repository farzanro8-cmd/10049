from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <script>
            async function updateData() {
                const res = await fetch('/data');
                const data = await res.json();
                document.getElementById('counter').innerText = data.counter;
                document.getElementById('value').innerText = data.value;
            }
            setInterval(updateData, 1000);
            window.onload = updateData;
        </script>
    </head>
    <body style="font-family: Arial; padding: 30px;">
        <h1>Live Data Dashboard</h1>
        <p><b>Counter:</b> <span id="counter">-</span></p>
        <p><b>Value:</b> <span id="value">-</span></p>
    </body>
    </html>
    """

@app.route("/data")
def data():
    return jsonify({
        "counter": int(time.time()),
        "value": random.randint(1, 100)
    })
