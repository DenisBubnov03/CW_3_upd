from blueprint.main import *
from blueprint.loader import *


POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"
app = Flask(__name__)
app.secret_key = 'super secret key'
app.register_blueprint(main_page)
app.register_blueprint(loader_blueprint)



@app.errorhandler(404)
@app.errorhandler(json.JSONDecodeError)
@app.errorhandler(FileNotFoundError)
def file_not_found(e):
    new_logger.error(f"Файл не найден или не может быть прочитан {e}")
    text = "Файл не найден или не может быть прочитан"
    return render_template('404.html', e=text)



@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":

    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()
