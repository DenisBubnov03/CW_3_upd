import pytest
from functions import get_comments_by_post_id, search_for_posts, get_post_by_pk, get_posts_by_user

"""Тесты функций"""


def test_get_int():
    with pytest.raises(TypeError):
        get_posts_by_user(2)


def test_no_found_name():
    with pytest.raises(ValueError):
        get_posts_by_user("din")


def test_get_str():
    with pytest.raises(TypeError):
        get_comments_by_post_id("two")


def test_no_found_comm():
    with pytest.raises(ValueError):
        get_comments_by_post_id(40)


def test_get_int_for_post():
    with pytest.raises(TypeError):
        search_for_posts(2)


def test_get_str_one_post():
    with pytest.raises(TypeError):
        get_post_by_pk("two")


def test_no_found_one_post():
    with pytest.raises(ValueError):
        get_post_by_pk(31)
