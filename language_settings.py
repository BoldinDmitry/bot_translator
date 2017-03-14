import config
import telebot
import json
from telebot import types
import yandexAPI


def change_language(message):
    """

    :param message: сообщение, которое отправил пользователь
    :return: вносит в базу данных настройки языка пользователя
    """
    database = {}
    bot = telebot.TeleBot(config.token)
    database[message.from_user.id] = message.text[-3:-1]
    database_json = json.dumps(database)
    file = open('database.json', 'w')
    file.write(database_json + '\n')
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, "now your translation language is" + message.text, reply_markup=markup)


def open_languages_settings(message):
    """

    :param message: сообщение, которое отправил пользователь
    :return: создает меню выбора языков
    """
    markup_list = []
    itembtn_name = []
    yandexAPI_list = list(yandexAPI.get_supported_languages())
    bot = telebot.TeleBot(config.token)
    markup = types.ReplyKeyboardMarkup(row_width=1)
    for i in range(len(yandexAPI_list)):
        itembtn_name.append('itmbtn' + str(i))
        itembtn_namei = types.KeyboardButton(": " + yandexAPI.get_supported_languages()[yandexAPI_list[i]] + '(' + yandexAPI_list[i] + ")")
        markup_list.append(itembtn_name[i])
        markup.add(itembtn_namei)
        i += 1
    print(markup_list)
    bot.send_message(message.chat.id, "Choose language:", reply_markup=markup)


def get_user_language(user_id):
    """

    :param user_id: id юзера
    :return: возвращает язык перевода конкретного юзера
    """
    file = json.load(open('database.json', 'r'))
    return file[str(user_id)]

