import telebot
from config import TG_token
from config import Proxy_config
from telebot import apihelper
from telebot import types

apihelper.proxy = Proxy_config
bot = telebot.TeleBot(TG_token)


buttons_name = ['добавить', 'удалить' , 'пример']


@bot.message_handler(commands=['start'])
def handle_start(message):
    keyboard = types.ReplyKeyboardMarkup(buttons_name)
    
    bot.reply_to(message, 'Привет! Я бот.', reply_markup=keyboard)


@bot.message_handler(commands=['stop'])
def handle_stop(message):
    bot.send_message(message.chat.id, "GoodBye Vika and Vika")
    
bot.polling(none_stop=True)