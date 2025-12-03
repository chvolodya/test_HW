import telebot
from config import TG_token
from config import Proxy_config
from telebot import apihelper
from telebot import types

apihelper.proxy = Proxy_config
bot = telebot.TeleBot(TG_token)


buttons_name = ['добавить', 'удалить' , 'пример', 'четвертая']


@bot.message_handler(commands=['start'])
def handle_start(message):
    
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    buttons = [types.KeyboardButton(i) for i in buttons_name]
    keyboard.add(*buttons)
    
       
    
    
    bot.reply_to(message, 'Привет! Я бот.', reply_markup=keyboard)


@bot.message_handler(commands=['stop'])
def handle_stop(message):
    bot.send_message(message.chat.id, "GoodBye Vika and Vovka")
    
bot.polling(none_stop=True)