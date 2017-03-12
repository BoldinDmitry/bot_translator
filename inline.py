import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)
yandex_icon = "https://lh5.ggpht.com/g40UQh7fmsg0oLRNpF4b06zeGBOwerbepCXTPz-HSwTSBBZzPODjzjJWkDUrX2v6p60=w300"
bot_icon = "https://telegram.org/file/811140614/2/flKQKZ7xUOE.27938.gif/5574a04570218c9e11"


def inline():
    @bot.inline_handler(lambda query: len(query.query) >= 0)
    def query_text(inline_query):
        bot = telebot.TeleBot(config.token)
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

if __name__ == '__main__':
    bot.polling(none_stop=True)