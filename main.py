
import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", "8080"))

web = Flask(__name__)

@web.get("/")
def home():
    return "Telegram bot is running!"

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "Hello! Bot is working successfully."
    )

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is missing")

    threading.Thread(
        target=lambda: web.run(
            host="0.0.0.0",
            port=PORT,
            use_reloader=False,
        ),
        daemon=True,
    ).start()

    bot = Application.builder().token(TOKEN).build()
    bot.add_handler(CommandHandler("start", start))
    bot.run_polling()

if __name__ == "__main__":
    main()
