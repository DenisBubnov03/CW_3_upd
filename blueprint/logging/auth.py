from flask import Blueprint, render_template, request, session, redirect
from uploads.images import *
from functions import get_data_json, new_logger, write_to_data
ALLOWED_EXTENSIONS = {'jpeg', 'png', 'jpg', 'gif'}
loader_blueprints = Blueprint('loader_blueprints', __name__)


@loader_blueprints.route('/reg/')
def loader_regg():
    """
    Переход на страницу /reg/
    """
    return render_template('reg.html')


@loader_blueprints.route("/reg/", methods=["POST"])
def registerr():
    """
    Регистрация и отработка ошибок
    """
    error = ''
    login = request.form.get('name_user')
    password = request.form.get('pass')
    avatar = request.files.get('avatar')
    filename = avatar.filename
    if not filename:
        filename = "default.png"
    extension = filename.split(".")[-1]
    for log in get_data_json():
        if login == log['login']:
            error = True
            new_logger.info("Введен повторяющийся логин")
            return render_template('Error_log.html', error_log=error)
    if extension not in ALLOWED_EXTENSIONS:
        error += "format"
        #добавить логгер
        return render_template('Error_log.html', error_format=error, format=", ".join(ALLOWED_EXTENSIONS))
    avatar.save(f"./static/img/{filename}")
    write_to_data(login, password, filename)
    session["key"] = login, filename
    return redirect('/')


@loader_blueprints.route("/logout/")
def logoutt():
    """
    Выход с аккаунта
    """
    session.clear()
    return redirect('/')


@loader_blueprints.route('/auth/')
def loader_loggs():
    """
    Переход на страницу с авторизацией
    """
    return render_template('auth.html')


@loader_blueprints.route('/auth/', methods=["POST"])
def logingg():
    """
    Отработка входа и обработка ошибок
    """
    login = request.form["name_user"]
    password = request.form["pass"]
    for x in get_data_json():
        if x['login'] == login:
            if x['pass'] == password:
                session["key"] = login
                new_logger.info(f"Пользователь {login} вошел в систему")
                return redirect('/')
    else:
        error = True
        new_logger.error(f"Пользователь {login} ввел неверный логин или пароль")
        return render_template('Error_log.html', error_pass=error)
