from flask import Flask, request, render_template, send_from_directory, Blueprint, session
from functions import *
import json


main_page = Blueprint('main_page', __name__)
add_pic = Blueprint('add_pic', __name__)

@main_page.route("/")
def page_index():
    """
    Загрузка главной страницы
    """
    post = get_json()
    if session.get('key'):
        return render_template("index.html", name_user=session["key"], posts=post)
    else:
        return render_template("index.html", posts=post)

