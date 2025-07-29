from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, CallbackContext

app = Flask(__name__)

# Your updated Telegram bot token
BOT_TOKEN = "8440109945:AAHsyuMmbKwD7lFOez9Fe86Zwjxzr0azCvo"

bot = Bot(token=BOT_TOKEN)
dispatcher = Dispatcher(bot=bot, update_queue=None, workers=1)

# /start command handler (single response)
def start(update: Update, context: CallbackContext):
    # To avoid duplicates, check for text and first-time
    if update.message and update.message.text:
        update.message.reply_text("✅ Hello! Nexora Auto Bot is working successfully.")

dispatcher.add_handler(CommandHandler("start", start))

# Telegram webhook handler
@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def handle_webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, bot)
    dispatcher.process_update(update)
    return "OK", 200

# Health-check endpoint for Render
@app.route("/", methods=["GET"])
def health_check():
    return "🚀 Nexora Auto Delivery Bot is running.", 200

if __name__ == "__main__":
    # Bind to all interfaces and port 10000
    app.run(host="0.0.0.0", port=10000)
