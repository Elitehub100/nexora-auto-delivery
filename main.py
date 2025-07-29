from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, CallbackContext

app = Flask(__name__)

BOT_TOKEN = "8440109945:AAHsyuMmbKwD7lFOez9Fe86Zwjxzr0azCvo"
SHOPPY_PRODUCT_URL = "https://shoppy.gg/product/Lz1YHRj"

bot = Bot(token=BOT_TOKEN)
dispatcher = Dispatcher(bot=bot, update_queue=None, workers=1)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("✅ Hello! Nexora Auto Bot is working successfully.")

dispatcher.add_handler(CommandHandler("start", start))

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def handle_webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "Webhook received!", 200

@app.route("/", methods=["GET"])
def health_check():
    return "🚀 Nexora Auto Delivery Bot is running on Render!", 200

# Shoppy webhook route for auto delivery
@app.route("/shoppy_webhook", methods=["POST"])
def shoppy_webhook():
    data = request.json
    
    # Adjust this key name to match what Shoppy sends for Telegram username
    telegram_username = data.get("buyer_telegram")  # Make sure your webhook includes this
    
    if telegram_username:
        try:
            bot.send_message(
                chat_id=f"@{telegram_username}",
                text=f"🎉 Thank you for your purchase!\nYour download link: {SHOPPY_PRODUCT_URL}"
            )
            return "Delivered", 200
        except Exception as e:
            print(f"Error sending message: {e}")
            return "Failed to send message", 500
    else:
        print("Telegram username missing in webhook payload.")
        return "Telegram username missing", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
