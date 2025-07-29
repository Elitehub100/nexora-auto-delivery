from flask import Flask, request
import requests

app = Flask(__name__)

# ✅ Your Telegram bot token (already replaced)
TOKEN = "8440109945:AAHsyuMmbKwD7lFOez9Fe86Zwjxzr0azCvo"
TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        # Auto-reply logic
        reply = f"✅ You said: {text}"
        requests.post(TELEGRAM_API, json={
            "chat_id": chat_id,
            "text": reply
        })

    return {"ok": True}

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
