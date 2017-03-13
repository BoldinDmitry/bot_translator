import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


@bot.inline_handler(lambda query: len(query.query) >= 0)
def query_text(inline_query):
    try:
        translation = types.InlineQueryResultArticle('1', 'translation', types.InputTextMessageContent('h'))
        suggestion = types.InlineQueryResultArticle('2', 'bot contact', types.InputTextMessageContent(
            'for language setup https://telegram.me/TranslateInBot'))
        bot.answer_inline_query(inline_query.id, [translation, suggestion])
    except Exception as e:
        print(e)


if __name__ == '__main__':
    bot.polling(none_stop=True)
