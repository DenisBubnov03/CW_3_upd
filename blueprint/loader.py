from flask import Blueprint, Flask, render_template, request, redirect, session
from functions import *

ALLOWED_EXTENSIONS = {'jpeg', 'png', 'jpg', 'gif'}
loader_blueprint = Blueprint('loader_blueprint', __name__)


@loader_blueprint.route('/reg/')
def loader_reg():
    """
    Переход на страницу /reg/
    """
    return render_template('reg.html')


@loader_blueprint.route("/reg/", methods=["POST"])
def register():
    """
    Регистрация и отработка ошибок
    """
    error = ""
    login = request.form.get('name_user')
    password = request.form.get('pass')
    for log in get_data_json():
        if login in log['login']:
            error += "true"
            new_logger.info("Введен повторяющийся логин")
            return render_template('Error_log.html', error_log=error)
    write_to_data(login, password)
    session["key"] = login
    return redirect('/')


@loader_blueprint.route("/logout/")
def logout():
    """
    Выход с аккаунта
    """
    session.clear()
    return redirect('/')


@loader_blueprint.route('/auth/')
def loader_log():
    """
    Переход на страницу с авторизацией
    """
    return render_template('auth.html')


@loader_blueprint.route('/auth/', methods=["POST"])
def loging():
    """
    Отработка входа и обработка ошибок
    """
    error = ""
    login = request.form["name_user"]
    password = request.form["pass"]
    for x in get_data_json():
        if x['login'] == login:
            if x['pass'] == password:
                session["key"] = login
                new_logger.info(f"Пользователь {login} вошел в систему")
                return redirect('/')
        else:
            error += "true"
            new_logger.error(f"Пользователь {login} ввел неверный логин или пароль")
            return render_template('Error_log.html', error_pass=error)


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
    error = ''
    picture = request.files.get("picture")
    filename = picture.filename
    extension = filename.split(".")[-1]
    if extension not in ALLOWED_EXTENSIONS:
        error += "format"
        new_logger.info("Неверный формат изображения")
        return render_template("Error_log.html", error_format=error, format=", ".join(ALLOWED_EXTENSIONS))
    if picture:
        picture.save(f"./uploads/images/{filename}")
        content = request.form['content']
        write_to_json(filename, content)
        return render_template("post_uploaded.html", content=content, picture=filename)
    else:
        error += "load"
        new_logger.info("Картинка не была выбрана")
        return render_template("Error_log.html", error_load=error)


@loader_blueprint.route('/search/')
def search_page():
    """
    Поиск постов по тегу
    """
    s = request.args.get('s')
    new_logger.info(f"Поиск по тегу: {s}")
    find_post = search_post(s)
    return render_template('post_list.html', search_word=s, posts=find_post)
