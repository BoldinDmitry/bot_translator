import requests
import keys
import json


def translate(language: str, text: str) -> str:
    """

    :param language: язык, на который необходимо перевести текст
    :param text: текст, который необходимо перевести
    :return: переведенный текст
    """
    link = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=" + keys.yandex_api_key + "&text=" + text \
           + "&lang=" + language
    answer = requests.get(link).text
    answer = json.loads(answer)
    #print(answer)
    if answer["code"] == 200:
        return answer["text"][0]
    else:
        return "error"


def get_supported_languages():
    link = "https://translate.yandex.net/api/v1.5/tr.json/getLangs?key=" + keys.yandex_api_key + "&ui=ru"
    answer = requests.get(link).text
    answer = json.loads(answer)
    return answer['langs']

#(get_supported_languages())