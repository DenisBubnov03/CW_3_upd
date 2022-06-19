from blueprint.loader import *
app = Flask(__name__)
app.register_blueprint(main_page)
app.register_blueprint(loader_blueprint)


@app.errorhandler(404)
@app.errorhandler(json.JSONDecodeError)
@app.errorhandler(FileNotFoundError)
@app.errorhandler(TypeError)
def file_not_found(e):
    new_logger.error(f"Файл не найден или не может быть прочитан {e}")
    text = "Файл не найден или не может быть прочитан"
    return render_template('404.html', e=text)


@app.errorhandler(500)
def error_server():
    text = "У нас, что-то сломалось, но мы скоро это починим"
    new_logger.error(f"Поломка на сервере")
    return render_template('500.html', e=text)


if __name__ == "__main__":
    app.run()
