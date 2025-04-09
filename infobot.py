import telebot
from telebot import types

TOKEN = "7311036196:AAFw2rWAtq1-G7_12j1NbzAzqGlrtVRSSfA"

ADMIN_CHAT_ID = -4692476565

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):    
    photo_url = 'https://imgur.com/YKsvgj4'
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Отправить «+»", url="https://t.me/Tanlauska")
    markup.add(button)

    bot.send_photo(message.chat.id, photo_url, caption="""
    Приветствуем вас! Благодарим, что перешли в нашего бота!
    Отправьте «+» нашему HR, и она расскажет всю информацию и проведёт от начала до конца на пути к заработку от 4000$ в месяц!👇🏻
    """, reply_markup=markup)

    username = message.from_user.username
    bot.send_message(ADMIN_CHAT_ID, f"Новый пользователь нажал /start: @{username}")

bot.polling()