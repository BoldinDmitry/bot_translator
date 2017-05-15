import config
import yandexAPI
import language_settings
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)
yandex_icon = "https://lh5.ggpht.com/g40UQh7fmsg0oLRNpF4b06zeGBOwerbepCXTPz-HSwTSBBZzPODjzjJWkDUrX2v6p60=w300"
bot_icon = "https://telegram.org/file/811140614/2/flKQKZ7xUOE.27938.gif/5574a04570218c9e11"


def handle_inline_query(bot, inline_query):
    yandex_icon = "https://lh5.ggpht.com/g40UQh7fmsg0oLRNpF4b06zeGBOwerbepCXTPz-HSwTSBBZzPODjzjJWkDUrX2v6p60=w300"
    bot_icon = "https://telegram.org/file/811140614/2/flKQKZ7xUOE.27938.gif/5574a04570218c9e11"

    language = language_settings.get_user_language(user_id=inline_query.from_user.id)
    translated_text = yandexAPI.translate(language, inline_query.query)
    translation = types.InlineQueryResultArticle(
        '1', 'translation', types.InputTextMessageContent(translated_text),
        thumb_url=yandex_icon, thumb_width=48, thumb_height=48
    )
    suggestion = types.InlineQueryResultArticle(
        '2', 'bot contact', types.InputTextMessageContent('for language setup https://telegram.me/TranslateInBot'),
        thumb_url=bot_icon, thumb_width=48, thumb_height=48
    )
    bot.answer_inline_query(inline_query.id, [translation, suggestion])

