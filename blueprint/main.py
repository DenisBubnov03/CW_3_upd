from flask import Flask, request, render_template, send_from_directory, Blueprint
from functions import *
app = Flask(__name__)

main_page = Blueprint('main_page', __name__)
add_pic = Blueprint('add_pic', __name__)

@main_page.route("/")
def page_index():
    """
    Загрузка главной страницы
    """
    return render_template("index.html")


