import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🥚 Steal a Egg Notifier запущен!\n\n"
        "Я буду отправлять уведомления о редких яйцах."
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 Статистика пока собирается.\n"
        "Когда появятся данные, здесь будет показан примерный интервал и частота."
    )

def main():
    if not TELEGRAM_TOKEN:
        raise RuntimeError("TELEGRAM_TOKEN не установлен")

    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))

    print("Bot started")
    app.run_polling()

if __name__ == "__main__":
    main()
