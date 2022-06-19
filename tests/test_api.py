from app import app

key = {"poster_name",
       "poster_avatar",
       "pic",
       "content",
       "views_count",
       "likes_count",
       "pk"}


def test_api():
    """Тест api"""
    response = app.test_client().get("/api/post/")
    assert isinstance(response.json, list), 'Неверный формат'
    for t in response.json:
        assert t.keys() == key, 'Ошибка в ключах'


def test_api_one():
    """Тесть api определенного поста"""
    response = app.test_client().get("/api/post/1")
    assert isinstance(response.json, dict), 'Неверный формат'
    assert response.json.keys() == key, 'Ошибка в ключах'



