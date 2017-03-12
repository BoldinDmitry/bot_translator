import config
import json
import telebot
from telebot import types
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id,  """\
Welkom to Translator bot settings, here you could set your translation language.\
""")
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('change language')
    itembtn2 = types.KeyboardButton('v')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, "you can:", reply_markup=markup)



@bot.message_handler(func=lambda message: message.text == 'change language')
def open_languge_setings(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('English')
    itembtn2 = types.KeyboardButton('French')
    itembtn3 = types.KeyboardButton('Russian')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Choose language:", reply_markup=markup)

@bot.message_handler(func=lambda message: len(message.text) > 0)
def change_language(message):
    user_data = json.dumps({"id": message.chat.id, "language": message.text}, sort_keys=True)
    file = open('text.txt', 'a')
    file.write(user_data + '\n')
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, "now your translation language is "+message.text, reply_markup=markup)





if __name__ == '__main__':
    bot.polling(none_stop=True)