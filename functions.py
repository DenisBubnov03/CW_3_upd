from flask import Flask, request, render_template, send_from_directory, Blueprint, session, jsonify
import json
import logging



def get_all_post():
    """
    Получение списка постов
    """
    with open('data/data.json', "r", encoding="UTF-8") as file:
        all_post = json.load(file)
        return all_post


def get_all_comments():
    """
    Получение списка комментариев
    """
    with open('data/comments.json', "r", encoding="UTF-8") as file:
        all_com = json.load(file)
        return all_com


def get_posts_by_user(user_name):
    """Поиск по имени"""
    posts = get_all_post()
    content = []
    user = []
    if type(user_name) not in [str]:
        raise TypeError("Должно быть 'str'")
    for p in posts:
        user.append(p["poster_name"])
        if user_name.lower() == p['poster_name']:
            content.append(p)
    if user_name not in user:
        raise ValueError("Такого пользователя нет")
    return content



def get_comments_by_post_id(post_id):
    """Возращение комментария определенного поста"""
    comments = get_all_comments()
    post = get_all_post()
    comment = []
    if type(post_id) not in [int]:
        raise TypeError("Должно быть 'int'")
    for c in comments:
        if post_id == c['post_id']:
            comment.append(c)
    for p in post:
        if post_id == p["pk"]:
            break
    else:
        raise ValueError("Такого комментария нет нет")
    return comment


def search_for_posts(query):
    """
    Поиск постов
    """
    post = get_all_post()
    content = []
    if type(query) not in [str]:
        raise TypeError("Должно быть 'str'")
    for s in post:
        if query.lower() in s["content"]:
            content.append(s)
        else:
            raise ValueError("Такого поста нет")
    return content


def get_post_by_pk(pk):
    """возвращает один пост по его идентификатору."""
    post = get_all_post()
    if type(pk) not in [int]:
        raise TypeError("Должно быть 'int'")
    for s in post:
        if s['pk'] == pk:
            return s
        else:
            raise ValueError("Такого поста нет")


new_logger = logging.getLogger('loger')
new_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("api.log", encoding='utf-8')
formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")
file_handler.setFormatter(formatter)
new_logger.addHandler(file_handler)

# def write_to_json(filename, content):
#     """
#     Добавление поста
#     """
#     data = get_all_post()
#     user_info = {'pic': f'/uploads/images/{filename}', "content": content}
#     data.append(user_info)
#     with open('posts.json', "w", encoding="UTF-8") as file:
#         json.dump(data, file, indent=4, ensure_ascii=False)
