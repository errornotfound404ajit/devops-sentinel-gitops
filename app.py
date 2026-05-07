from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps Sentinel AI Running 🚀"

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/fail")
def fail():
    if random.random() > 0.5:
        return 1/0
    return "No failure this time"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
