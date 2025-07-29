from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Set your bot token here
BOT_TOKEN = "8440109945:AAHsyuMmbKwD7lFOez9Fe86Zwjxzr0azCvo"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# To prevent duplicate /start responses, track last update_id processed
last_update_id = None

@app.route('/webhook', methods=['POST'])
def webhook():
    global last_update_id

    data = request.get_json()

    # Ensure update_id is new
    update_id = data.get("update_id")
    if update_id == last_update_id:
        # Duplicate update, ignore
        return "ok", 200
    last_update_id = update_id

    message = data.get("message")
    if not message:
        return "no message", 200

    chat_id = message['chat']['id']
    text = message.get('text', '')

    # Handle /start command
    if text == "/start":
        send_message(chat_id, "✅ Hello! Nexora Auto Bot is working successfully.")
    else:
        send_message(chat_id, "Unknown command.")

    return "ok", 200

def send_message(chat_id, text):
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(TELEGRAM_API_URL, json=payload)

if __name__ == "__main__":
    # Use port from environment variable for Render compatibility
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
