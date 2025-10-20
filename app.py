from flask import Flask, request
import requests, json, os

app = Flask(__name__)

# Environment variables from Render
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")  # Example: -1002607718600 (for a channel)

print("Loaded BOT_TOKEN:", BOT_TOKEN)
print("Loaded CHAT_ID:", CHAT_ID)

@app.route("/")
def home():
    return "✅ Canva Webhook Receiver Active"

@app.route("/canva-webhook", methods=["POST"])
def canva_webhook():
    data = request.get_json()
    print("Received from Canva:", json.dumps(data, indent=2))

    # Prepare message in HTML format (Telegram-safe)
    message = f"📢 <b>Canva Incident Update</b>\n\n<pre>{json.dumps(data, indent=2)}</pre>"

    # Send to Telegram channel
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = requests.post(
        telegram_url,
        data={
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "HTML",
            "disable_web_page_preview": True
        }
    )

    # Log Telegram response for debugging
    print("Telegram response:", response.text)

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
