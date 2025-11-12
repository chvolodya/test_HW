import telebot
from config import TG_token
bot = telebot.TeleBot(TG_token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Hello Vika and Vovka")
    bot.send_message(message.chat.id, "Branch Test")

bot.polling(none_stop=True)