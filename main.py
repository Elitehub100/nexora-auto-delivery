from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, CallbackContext

app = Flask(__name__)

# Your Bot Token (keep it secret!)
BOT_TOKEN = "8440109945:AAHsyuMmbKwD7lFOez9Fe86Zwjxzr0azCvo"

bot = Bot(token=BOT_TOKEN)

# Dispatcher with 1 worker to avoid async issues on Render
dispatcher = Dispatcher(bot=bot, update_queue=None, workers=1, use_context=True)

# Command handler for /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("✅ Hello! Nexora Auto Bot is working successfully.")

dispatcher.add_handler(CommandHandler("start", start))

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK", 200

@app.route("/", methods=["GET"])
def health_check():
    return "🚀 Nexora Auto Delivery Bot is running!", 200

if __name__ == "__main__":
    # Bind to 0.0.0.0 so Render can route traffic
    app.run(host="0.0.0.0", port=10000)
