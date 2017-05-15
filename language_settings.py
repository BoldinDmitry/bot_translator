import config
import telebot
import json
from telebot import types
import yandexAPI
markup = types.ReplyKeyboardMarkup(row_width=1)
yandexAPI_list = list(yandexAPI.get_supported_languages())
markup_list = []
itembtn_name = []
for i in range(len(yandexAPI_list)):
    itembtn_name.append('itmbtn' + str(i))
    itembtn_namei = types.KeyboardButton(
        ": " + yandexAPI.get_supported_languages()[yandexAPI_list[i]] + '(' + yandexAPI_list[i] + ")")
    markup_list.append(itembtn_name[i])
    markup.add(itembtn_namei)


def change_language(message):
    """

    :param message: сообщение, которое отправил пользователь
    :return: вносит в базу данных настройки языка пользователя
    """
    bot = telebot.TeleBot(config.token)
    with open('database.json') as file:
        database = json.load(file)
    database[message.from_user.id] = message.text[-3:-1]
    # file.close()
    file = open('database.json', 'w')
    file.write(json.dumps(database))
    file.close()
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, "now your translation language is" + message.text, reply_markup=markup)


def open_languages_settings(message):
    """

    :param message: сообщение, которое отправил пользователь
    :return: создает меню выбора языков
    """
    bot = telebot.TeleBot(config.token)
    #print(markup_list)
    bot.send_message(message.chat.id, "Choose language:", reply_markup=markup)


def get_user_language(user_id):
    """

    :param user_id: id юзера
    :return: возвращает язык перевода конкретного юзера
    """
    with open('database.json') as file:
        database = json.load(file)
        print(database)
        print(user_id)
        language = database.get(str(user_id))
        print(language)
    return language

