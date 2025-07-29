import os
from flask import Flask, request, jsonify
from telegram import Bot
from threading import Lock

app = Flask(__name__)

# Your Telegram bot token and chat ID
bot_token = '8440109945:AAHsyuMmbKwD7lFOez9Fe86Zwjxzr0azCvo'
chat_id = '5468345098'

bot = Bot(token=bot_token)
sent_ids = set()
lock = Lock()

@app.route("/", methods=["POST"])
def handle_delivery():
    data = request.get_json()

    if not data or "id" not in data or "file" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    delivery_id = data["id"]
    file_name = data["file"]

    with lock:
        if delivery_id in sent_ids:
            message = f"⚠️ Duplicate Delivery Detected!\nDelivery ID: `{delivery_id}`\nFile: `{file_name}`"
        else:
            sent_ids.add(delivery_id)
            message = f"✅ New Digital File Delivered!\n📦 File: `{file_name}`\n🆔 Delivery ID: `{delivery_id}`"

    try:
        bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')
        return jsonify({"status": "Message sent"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=False, port=10000, host="0.0.0.0")
