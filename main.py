from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8440109945:AAHsyuMmbKwD7lFOez9Fe86Zwjxzr0azCvo"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

# Prevent duplicate replies
responded_users = set()

@app.route('/')
def home():
    return '✅ Nexora Auto Delivery Bot is Running!'

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def telegram_webhook():
    data = request.get_json()
    if "message" in data and "text" in data["message"]:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]
        if text == "/start" and chat_id not in responded_users:
            send_message(chat_id, "✅ Hello! Nexora Auto Bot is working successfully.")
            responded_users.add(chat_id)
    return "OK"

def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(debug=False)
