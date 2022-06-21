from functions import *
loader_blueprint = Blueprint('loader_blueprint', __name__)
main_page = Blueprint('main_page', __name__)
ALLOWED_EXTENSIONS = {'jpeg', 'png', 'jpg', 'gif'}
app = Flask(__name__)


@loader_blueprint.route("/api/post/")
def all_post():
    """Вывод api страницы"""
    post = get_all_post()
    new_logger.info("Запрос /api/post/")
    return jsonify(post)


@loader_blueprint.route("/api/post/<int:post_id>", methods=["GET"])
def get_post(post_id):
    """Вывод api страницы определенного поста"""
    post = get_post_by_pk(post_id)
    new_logger.info(f'Запрос /api/post/{post_id}')
    return jsonify(post)


@main_page.route("/")
def page_index():
    """
    Загрузка главной страницы"закоменчено будущее обновление"
    """
    post = get_all_post()
    if session.get('key'):
        return render_template("index.html", name_user=session["key"][0], user_avatar=session["key"][1], posts=post)
    else:
        return render_template("index.html", posts=post)


@loader_blueprint.route('/post/<int:pk>', methods=["GET"])
def loader_page(pk):
    """
    Переход на страницу /post/
    """
    comm = get_comments_by_post_id(pk)
    get_post = get_post_by_pk(pk)
    return render_template('post.html', post=get_post, comm=comm, len_com=len(comm))


@loader_blueprint.route('/search/', methods=['GET'])
def search_page():
    """
    Поиск постов по тегу
    """
    find_post = []
    if request.args.get("s"):
        s = request.args.get('s')
        find_post = search_for_posts(s)
    return render_template('search.html', posts=find_post)


@loader_blueprint.route('/user/<username>')
def get_user(username):
    """Вывод старинцы определенного пользователя"""
    post = get_posts_by_user(username)
    return render_template('user-feed.html', post=post)


@loader_blueprint.route('/poster/')
def loader_pages():
    """
    Переход на страницу /add_post/
    """
    return render_template("post_form.html", name_user=session["key"])


@loader_blueprint.route("/poster/", methods=["POST"])
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
        return render_template("Error_log.html",  )
    if picture:
        picture.save(f"./uploads/images/{filename}")
        content = request.form['content']
        write_to_json(filename, content)
        return render_template("post_form.html", content=content, name_user=session["key"][0], picture=filename)
    else:
        error += "load"
        new_logger.info("Картинка не была выбрана")
        return render_template("Error_log.html", error_load=error)