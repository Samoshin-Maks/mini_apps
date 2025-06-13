import requests

# === ЗАМЕНИ ЭТИ ДАННЫЕ НА СВОИ ===
TOKEN = '7625539703:AAF7nDtV5vndTY2pqREfTkqO4oTv7D13S1Q'  # токен от BotFather
CHAT_ID = '428172090'  # ID из @userinfobot
WEBAPP_URL = 'https://mini-apps-ebon.vercel.app/'  # ссылка на твой мини-сайт

# === ТЕКСТ СООБЩЕНИЯ И КНОПКИ ===
data = {
    "chat_id": CHAT_ID,
    "text": "Нажми кнопку, чтобы открыть мини-приложение:",
    "reply_markup": {
        "inline_keyboard": [[{
            "text": "Открыть Mini App 🚀",
            "web_app": {
                "url": WEBAPP_URL
            }
        }]]
    }
}

# === ОТПРАВКА СООБЩЕНИЯ ===
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
response = requests.post(url, json=data)

# === ПЕЧАТЬ РЕЗУЛЬТАТА ===
if response.ok:
    print("Кнопка успешно отправлена ✅")
else:
    print("Ошибка ❌", response.text)