import config
import inline_moduel
import language_settings
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


@bot.inline_handler(lambda query: len(query.query) >= 0)
def inline_handle(inline_query):
    inline_moduel.handle_inline_query(bot, inline_query)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, """\
Welcome to Translator bot settings, here you could set your translation language.\
""")
    markup = types.ReplyKeyboardMarkup(row_width=1)
    welcome_button1 = types.KeyboardButton('change language')
    welcome_button2 = types.KeyboardButton('other option')
    markup.add(welcome_button1, welcome_button2)
    bot.send_message(message.chat.id, "you can:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'change language')
def message_handler(message):
    language_settings.open_languages_settings(message)


@bot.message_handler(func=lambda message: message.text[0] == ':')
def message_handler(message):
    language_settings.change_language(message)


if __name__ == '__main__':
    bot.polling(none_stop=True)