from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

TOKEN = "8440109945:AAH4xiOzPE8M-seLUPUofgPvIuRJBcHjGJM"
bot = Bot(token=TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

def start(update, context):
    update.message.reply_text("👋 Welcome to Nexora Auto Bot!")

def help_command(update, context):
    update.message.reply_text("💡 Send a product code to get your digital product.")

dispatcher = Dispatcher(bot, None, workers=0, use_context=True)
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help_command))

if __name__ == "__main__":
    app.run(port=5000)
