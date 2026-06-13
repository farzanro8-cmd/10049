from flask import Flask
import random
import time

app = Flask(__name__)

@app.route("/")
def home():
    counter = int(time.time())
    value = random.randint(1, 100)

    return f"""
    <html>
    <head>
        <meta http-equiv="refresh" content="1">
        <title>Live Data</title>
    </head>
    <body style="font-family: Arial; padding: 30px;">
        <h1>Live Data Dashboard</h1>
        <p><b>Counter:</b> {counter}</p>
        <p><b>Value:</b> {value}</p>
        <p>Page refreshes every 1 second.</p>
    </body>
    </html>
    """
