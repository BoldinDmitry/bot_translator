def open_languages_settings(message):
    bot = telebot.TeleBot(config.token)
    keyboard = types.InlineKeyboardMarkup()
    #markup = types.ReplyKeyboardMarkup(row_width=1)
    for i in range(90):
        itembtn_name.append('itmbtn' + str(i))
        itembtn_namei = types.InlineKeyboardButton(
            ": " + yandexAPI.get_supported_languages()[yandexAPI_list[i]], callback_data=yandexAPI_list[i]
                                                   )
        markup_list.append(itembtn_name[i])
        keyboard.add(itembtn_namei)
        i += 1
    print(markup_list)
    bot.send_message(message.chat.id, "Choose language:", reply_markup=keyboard)