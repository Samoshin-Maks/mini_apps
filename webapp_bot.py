from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# === ЗАМЕНИ НА СВОИ ДАННЫЕ ===
BOT_TOKEN = '7625539703:AAF7nDtV5vndTY2pqREfTkqO4oTv7D13S1Q'  # токен от BotFather
WEBAPP_URL = 'https://mini-apps-ebon.vercel.app/'  # URL твоего мини-приложения

# === ОБРАБОТЧИК КОМАНДЫ /start ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Открыть Mini App 🚀", web_app=WebAppInfo(url=WEBAPP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Нажми на кнопку ниже, чтобы открыть мини-приложение:", reply_markup=reply_markup)

# === ЗАПУСК БОТА ===
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Бот запущен... Ожидает команду /start")
    app.run_polling()