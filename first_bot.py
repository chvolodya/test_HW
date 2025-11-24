import telebot
from config import TG_token
bot = telebot.TeleBot(TG_token)

from telebot import types

buttons_name = ['добавить', 'удалить' , 'пример']


@bot.message_handler(commands=['start'])
def handle_start(message):
    keyboard = types.ReplyKeyboardMarkup(buttons_name)
    
    bot.reply_to(message, 'Привет! Я бот.', reply_markup=keyboard)


@bot.message_handler(commands=['stop'])
def handle_stop(message):
    bot.send_message(message.chat.id, "GoodBye Vika and Vovka")
    
bot.polling(none_stop=True)
