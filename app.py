from flask import Flask, request
import requests, json

app = Flask(__name__)

BOT_TOKEN = "8405557217:AAFL91qvTZ26Zd-C1PGw9tJgi6WzcOJTkYs"
CHAT_ID = "-2072607718600"

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
        f"https://api.telegram.org/bot{8405557217:AAFL91qvTZ26Zd-C1PGw9tJgi6WzcOJTkYs}/sendMessage",
        data={"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    )
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
