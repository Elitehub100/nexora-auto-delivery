from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, CallbackContext

app = Flask(__name__)

BOT_TOKEN = "8440109945:AAHsyuMmbKwD7lFOez9Fe86Zwjxzr0azCvo"
bot = Bot(token=BOT_TOKEN)
dispatcher = Dispatcher(bot=bot, update_queue=None, workers=1)

# Your Shoppy product URL
SHOPPY_PRODUCT_URL = "https://shoppy.gg/product/Lz1YHRj"

# /start command handler
def start(update: Update, context: CallbackContext):
    welcome_msg = (
        "✅ Welcome to Nexora Auto Bot!\n\n"
        f"🛒 Buy the toolkit here: {SHOPPY_PRODUCT_URL}\n"
        "📦 After payment, your file will be delivered instantly.\n\n"
        "💬 Need help? Message @Nimona111"
    )
    update.message.reply_text(welcome_msg)

# Register handler
dispatcher.add_handler(CommandHandler("start", start))

# Webhook route
@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok", 200

# Health check route
@app.route("/", methods=["GET"])
def health_check():
    return "🚀 Nexora Auto Delivery Bot is running!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
