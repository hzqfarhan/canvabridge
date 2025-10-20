from flask import Flask, request
import requests, json

app = Flask(__name__)

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


@app.route("/")
def home():
    return "✅ Canva Webhook Receiver Active"

@app.route("/canva-webhook", methods=["POST"])
def canva_webhook():
    data = request.get_json()
    print("Received from Canva:", json.dumps(data, indent=2))

    # Convert Canva data into readable text
    message = f"📢 *Canva Incident Update*\n\n```{json.dumps(data, indent=2)}```"

    # Send message to Telegram
    requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
)

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
