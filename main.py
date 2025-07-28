from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

# ✅ Your updated Telegram Bot Token
TOKEN = "8440109945:AAHsyuMmbKwD7lFOez9Fe86Zwjxzr0azCvo"

bot = Bot(token=TOKEN)
app = Flask(__name__)

# ✅ Home route to check server status
@app.route('/')
def home():
    return "🤖 Nexora Auto Bot is live!"

# ✅ Webhook route – must match your bot token
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

# ✅ /start command
def start(update, context):
    update.message.reply_text("👋 Welcome to Nexora Auto Bot!")

# ✅ /help command
def help_command(update, context):
    update.message.reply_text("💡 Send a product code to get your digital product.")

# ✅ Register handlers
dispatcher = Dispatcher(bot, None, workers=0, use_context=True)
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help_command))

if __name__ == "__main__":
    app.run(port=5000)
