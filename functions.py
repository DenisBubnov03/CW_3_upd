import json
from flask import render_template, abort
import logging


def get_data_json():
    """
    Получение данных пользователей
    """
    with open('user_data.json', "r", encoding="UTF-8") as file:
        data = json.load(file)
        return data


def get_json():
    """
    Получение списка постов
    """
    with open('posts.json', "r", encoding="UTF-8") as file:
        all_post = json.load(file)
        return all_post


def search_post(text):
    """
    Поиск постов
    """
    post = get_json()
    content = []
    for s in post:
        if text in s["content"]:
            content.append(s)
    return content


def write_to_json(filename, content):
    """
    Добавление поста
    """
    data = get_json()
    user_info = {'pic': f'/uploads/images/{filename}', "content": content}
    data.append(user_info)
    with open('posts.json', "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)





def write_to_data(login, password):
    """
    Запись данных пользователя
    """
    data = get_data_json()
    user_info = {'login': login, "pass": password}
    data.append(user_info)
    with open('user_data.json', "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


new_logger = logging.getLogger('loger')
new_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("basic.log", encoding='utf-8')
formatter = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s")
file_handler.setFormatter(formatter)
new_logger.addHandler(file_handler)

