from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = "8440109945:AAHsyuMmbKwD7lFOez9Fe86Zwjxzr0azCvo"
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def receive_update():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        message_text = data["message"].get("text", "")

        if message_text.lower() == "/start":
            send_message(chat_id, "✅ Hello! Nexora Auto Bot is working successfully.")
        else:
            send_message(chat_id, f"✅ Received: {message_text}")

    return {"ok": True}

def send_message(chat_id, text):
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(API_URL, json=payload)

# ✅ Fix for Render Deployment: bind to 0.0.0.0 and dynamic port
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
