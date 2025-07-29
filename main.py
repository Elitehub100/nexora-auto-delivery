from flask import Flask, request, send_file
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = "8440109945:AAHsyuMmbKwD7lFOez9Fe86Zwjxzr0azCvo"
TELEGRAM_API = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

# Prevents duplicate responses
last_update_id = None

@app.route("/")
def home():
    return "✅ Nexora Auto Bot is Live!"

@app.route(f"/{TELEGRAM_TOKEN}", methods=["POST"])
def webhook():
    global last_update_id
    data = request.get_json()

    if not data:
        return "No data", 400

    update_id = data.get("update_id")
    if update_id == last_update_id:
        return "Duplicate update", 200
    last_update_id = update_id

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            send_message(chat_id, "👋 Welcome to Nexora Auto Bot!\nUse /help to see commands.")
        elif text == "/help":
            send_message(chat_id, "📘 *Available Commands:*\n/start – Start the bot\n/help – Show help\n/status – Check bot status\n/download – Get EliteToolkit.zip", parse_mode="Markdown")
        elif text == "/status":
            send_message(chat_id, "✅ Bot is running and active!")
        elif text == "/download":
            send_document(chat_id, "EliteToolkit.zip", "EliteToolkit.zip")
        else:
            send_message(chat_id, "❓ Unknown command. Use /help for available options.")

    return "OK", 200

def send_message(chat_id, text, parse_mode=None):
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    if parse_mode:
        payload["parse_mode"] = parse_mode
    requests.post(f"{TELEGRAM_API}/sendMessage", json=payload)

def send_document(chat_id, filename, caption=None):
    try:
        with open(filename, 'rb') as file:
            files = {'document': (filename, file)}
            data = {
                "chat_id": chat_id,
                "caption": caption or filename
            }
            requests.post(f"{TELEGRAM_API}/sendDocument", data=data, files=files)
    except FileNotFoundError:
        send_message(chat_id, "❌ File not found: EliteToolkit.zip")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
