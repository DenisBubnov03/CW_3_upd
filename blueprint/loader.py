from functions import *
loader_blueprint = Blueprint('loader_blueprint', __name__)
main_page = Blueprint('main_page', __name__)


@loader_blueprint.route("/api/post")
def all_post():
    new_logger.info("Запроси /api/post")
    return jsonify(get_all_post())


@loader_blueprint.route("/api/post/<int:post_id>", methods=["GET"])
def get_post(post_id):
    post = get_post_by_pk(post_id)
    new_logger.info(f'Запрос /api/post/{post_id}')
    return jsonify(post)


@main_page.route("/")
def page_index():
    """
    Загрузка главной страницы
    """
    post = get_all_post()
    # if session.get('key'):
    #     return render_template("index.html", name_user=session["key"], posts=post)
    # else:
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
    post = get_posts_by_user(username)
    return render_template('user-feed.html', post=post)
