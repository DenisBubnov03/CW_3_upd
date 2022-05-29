from flask import Blueprint, Flask, render_template, request
from functions import *


app = Flask(__name__)
ALLOWED_EXTENSIONS = {'jpeg', 'png', 'jpg', 'gif'}
loader_blueprint = Blueprint('loader_blueprint', __name__)




@loader_blueprint.route('/post/')
def loader_page():
    """
    Переход на страницу /post/
    """
    return render_template('post_form.html')


@loader_blueprint.route("/post/", methods=["POST"])
def page_post_upload():
    """
    Отработка страницы добавления поста и обработка ошибок
    """
    picture = request.files.get("picture")
    filename = picture.filename
    extension = filename.split(".")[-1]
    if extension not in ALLOWED_EXTENSIONS:
        new_logger.info("Неверный формат изображения")
        return ("Неверный формат изображения")
    if picture:
        picture.save(f"./uploads/images/{filename}")
        content = request.form['content']
        write_to_json(filename, content)
        return render_template("post_uploaded.html", content=content, picture=filename)
    else:
        new_logger.info("Картинка не была выбрана")
        return ("Ошибка загрузки")


@loader_blueprint.route('/search/')
def search_page():
    """
    Поиск постов по тегу
    """
    s = request.args.get('s')
    new_logger.info(f"Поиск по тегу: {s}")
    find_post = search_post(s)
    return render_template('post_list.html', search_word=s, posts=find_post)
