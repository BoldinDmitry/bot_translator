import requests


def detect_language(text):

    link = "https://translate.yandex.net/api/v1.5/tr.json/detect?key=<API-ключ>& text=<текст>"
