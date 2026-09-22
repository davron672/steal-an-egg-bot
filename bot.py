import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


TOKEN = os.environ.get("TELEGRAM_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🥚 Steal An Egg Notifier запущен!\n\n"
        "Я готов получать уведомления."
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 Статистика пока собирается."
    )


def main():
    if not TOKEN:
        raise RuntimeError("TELEGRAM_TOKEN не найден в Environment Variables")

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("status", status))

    print("Bot started successfully")

    application.run_polling(
        allowed_updates=Update.ALL_TYPES
    )


if __name__ == "__main__":
    main()
