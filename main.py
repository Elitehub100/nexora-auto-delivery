import os
from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '8440109945:AAHsyuMmbKwD7lFOez9Fe86Zwjxzr0azCvo'
TELEGRAM_API = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'

@app.route(f'/{BOT_TOKEN}', methods=["POST"])
def webhook():
    update = request.get_json()

    if "message" in update:
        message = update["message"]
        chat_id = message["chat"]["id"]
        text = message.get("text", "")

        if text == "/start":
            reply_text = "✅ Hello! Nexora Auto Bot is working successfully."
            send_message(chat_id, reply_text)

    return {"ok": True}

def send_message(chat_id, text):
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(TELEGRAM_API, json=payload)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render's PORT
    app.run(host='0.0.0.0', port=port)
