import config
import json
import telebot
from telebot import types
bot = telebot.TeleBot(config.token)


@bot.inline_handler(lambda query: len(query.query) >= 0)
def query_text(inline_query):
    yandex_icon = "https://lh5.ggpht.com/g40UQh7fmsg0oLRNpF4b06zeGBOwerbepCXTPz-HSwTSBBZzPODjzjJWkDUrX2v6p60=w300"
    bot_icon = "https://telegram.org/file/811140614/2/flKQKZ7xUOE.27938.gif/5574a04570218c9e11"
    try:
        translation = types.InlineQueryResultArticle(
            '1', 'translation', types.InputTextMessageContent('translated_text'),
        thumb_url = yandex_icon, thumb_width = 48, thumb_height = 48
        )
        suggestion = types.InlineQueryResultArticle(
            '2', 'bot contact', types.InputTextMessageContent('for language setup https://telegram.me/TranslateInBot'),
            thumb_url=bot_icon, thumb_width=48, thumb_height=48
        )
        bot.answer_inline_query(inline_query.id, [translation, suggestion])
    except Exception as e:
        print(e)


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