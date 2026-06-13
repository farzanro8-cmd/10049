from flask import Flask
import subprocess
import threading

app = Flask(__name__)

logs = []

def run_script():
    process = subprocess.Popen(
        ["python", "worker.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )

    for line in process.stdout:
        line = line.strip()
        print(line)          # همچنان در ترمینال دیده می‌شود
        logs.append(line)    # ذخیره برای وب

        if len(logs) > 100:
            logs.pop(0)

threading.Thread(target=run_script, daemon=True).start()

@app.route("/")
def home():
    log_html = "<br>".join(logs[::-1])

    return f"""
    <html>
    <head>
        <meta http-equiv="refresh" content="1">
        <title>Live Logs</title>
    </head>
    <body style="background:#111;color:#0f0;font-family:monospace;padding:20px">
        <h2>Live Python Logs</h2>
        {log_html}
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
