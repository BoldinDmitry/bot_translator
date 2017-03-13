import config
import telebot
import json
from telebot import types


def change_language(message):
    bot = telebot.TeleBot(config.token)
    user_data = json.dumps({"id": message.chat.id, "language": message.text}, sort_keys=True)
    file = open('database.json', 'a')
    file.write(user_data + '\n')
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, "now your translation language is " + message.text, reply_markup=markup)


def open_languages_settings(message):
    bot = telebot.TeleBot(config.token)
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton(':English')
    itembtn2 = types.KeyboardButton(':French')
    itembtn3 = types.KeyboardButton(':Russian')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Choose language:", reply_markup=markup)
