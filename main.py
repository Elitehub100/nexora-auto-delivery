from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, CallbackContext

app = Flask(__name__)

# Your bot token
BOT_TOKEN = "8440109945:AAHsyuMmbKwD7lFOez9Fe86Zwjxzr0azCvo"

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dispatcher = Dispatcher(bot=bot, update_queue=None, workers=1)

# Command: /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("✅ Hello! Nexora Auto Bot is working successfully.")

# Register the command handler
dispatcher.add_handler(CommandHandler("start", start))

# Webhook endpoint
@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def handle_webhook():
    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
        return "Webhook received!", 200

# Health check endpoint
@app.route("/", methods=["GET"])
def health_check():
    return "🚀 Nexora Auto Delivery Bot is running on Render!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
