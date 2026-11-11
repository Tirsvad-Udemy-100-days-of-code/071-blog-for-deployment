"""! @file test_blog_flow.py
@brief End-to-end tests through the Flask test client (in-memory SQLite, CSRF off).
"""
import re
from collections.abc import Iterator

import pytest
from flask import Flask
from flask.testing import FlaskClient

from presentation import create_app
from presentation.sanitizer import sanitize_html

POST = {"title": "Hello", "subtitle": "World", "img_url": "", "body": "<p>Body text</p>"}


@pytest.fixture
def app() -> Iterator[Flask]:
    yield create_app({"TESTING": True, "WTF_CSRF_ENABLED": False})


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


def _register(client: FlaskClient, email: str, name: str) -> None:
    client.post("/register", data={"email": email, "password": "pw", "name": name})


def _admin_client(app: Flask) -> FlaskClient:
    admin = app.test_client()
    _register(admin, "admin@example.com", "Admin")
    return admin


def test_register_logs_user_in_and_shows_logout(client: FlaskClient) -> None:
    response = client.post(
        "/register", data={"email": "a@example.com", "password": "pw", "name": "A"}, follow_redirects=True
    )
    assert b"Log Out" in response.data


def test_register_duplicate_email_redirects_to_login_with_message(app: Flask) -> None:
    _admin_client(app)
    response = app.test_client().post(
        "/register", data={"email": "admin@example.com", "password": "x", "name": "B"}, follow_redirects=True
    )
    assert b"already signed up" in response.data


def test_login_with_wrong_password_shows_error(app: Flask) -> None:
    _admin_client(app)
    response = app.test_client().post("/login", data={"email": "admin@example.com", "password": "bad"})
    assert b"Invalid email or password" in response.data


def test_logout_then_login_works_and_nav_changes(app: Flask) -> None:
    admin = _admin_client(app)
    assert b"Login" in admin.get("/logout", follow_redirects=True).data
    response = admin.post(
        "/login", data={"email": "admin@example.com", "password": "pw"}, follow_redirects=True
    )
    assert b"New Post" in response.data


def test_admin_creates_post_and_reader_sees_it(app: Flask) -> None:
    admin = _admin_client(app)
    assert admin.post("/new-post", data=POST).status_code == 302
    reader = app.test_client()
    assert b"Hello" in reader.get("/").data
    assert b"Body text" in reader.get("/post/1").data


def test_second_user_comments_and_comment_is_shown(app: Flask) -> None:
    _admin_client(app).post("/new-post", data=POST)
    second = app.test_client()
    _register(second, "b@example.com", "Bob")
    second.post("/post/1", data={"comment_text": "<p>Great read</p>"})
    page = second.get("/post/1").data
    assert b"Great read" in page and b"Bob" in page


def test_second_user_gets_403_on_new_post(app: Flask) -> None:
    _admin_client(app)
    second = app.test_client()
    _register(second, "b@example.com", "Bob")
    assert second.get("/new-post").status_code == 403
    assert second.post("/new-post", data=POST).status_code == 403


def test_anonymous_gets_403_on_edit_and_delete(app: Flask) -> None:
    _admin_client(app).post("/new-post", data=POST)
    anonymous = app.test_client()
    assert anonymous.get("/edit-post/1").status_code == 403
    assert anonymous.post("/delete/1").status_code == 403


def test_anonymous_comment_redirects_to_login(app: Flask) -> None:
    _admin_client(app).post("/new-post", data=POST)
    response = app.test_client().post("/post/1", data={"comment_text": "hi"})
    assert response.status_code == 302 and "/login" in response.headers["Location"]


def test_admin_edits_post(app: Flask) -> None:
    admin = _admin_client(app)
    admin.post("/new-post", data=POST)
    admin.post("/edit-post/1", data={**POST, "title": "Changed"})
    assert b"Changed" in admin.get("/post/1").data


def test_admin_deletes_post_and_it_disappears(app: Flask) -> None:
    admin = _admin_client(app)
    admin.post("/new-post", data=POST)
    assert admin.post("/delete/1").status_code == 302
    assert admin.get("/post/1").status_code == 404


def test_delete_with_get_returns_405_for_admin(app: Flask) -> None:
    admin = _admin_client(app)
    admin.post("/new-post", data=POST)
    assert admin.get("/delete/1").status_code == 405
    assert admin.get("/post/1").status_code == 200


def test_non_admin_post_to_delete_returns_403(app: Flask) -> None:
    _admin_client(app).post("/new-post", data=POST)
    second = app.test_client()
    _register(second, "b@example.com", "Bob")
    assert second.post("/delete/1").status_code == 403


def test_delete_missing_post_returns_404(app: Flask) -> None:
    assert _admin_client(app).post("/delete/99").status_code == 404


def _csrf_token(client: FlaskClient, path: str) -> str:
    match = re.search(r'name="csrf_token"[^>]*value="([^"]+)"', client.get(path).get_data(as_text=True))
    assert match is not None
    return match.group(1)


def test_delete_requires_csrf_token_when_protection_enabled() -> None:
    app = create_app({"TESTING": True, "WTF_CSRF_ENABLED": True})
    admin = app.test_client()
    admin.post(
        "/register",
        data={"email": "admin@example.com", "password": "pw", "name": "Admin", "csrf_token": _csrf_token(admin, "/register")},
    )
    admin.post("/new-post", data={**POST, "csrf_token": _csrf_token(admin, "/new-post")})
    assert admin.post("/delete/1").status_code == 400
    assert admin.get("/post/1").status_code == 200
    assert admin.post("/delete/1", data={"csrf_token": _csrf_token(admin, "/")}).status_code == 302
    assert admin.get("/post/1").status_code == 404


def test_missing_post_returns_404(client: FlaskClient) -> None:
    assert client.get("/post/99").status_code == 404


def test_script_in_post_body_is_stripped_on_write(app: Flask) -> None:
    admin = _admin_client(app)
    admin.post("/new-post", data={**POST, "body": "<p>ok</p><script>alert(1)</script>"})
    page = admin.get("/post/1").data
    assert b"alert(1)" not in page and b"ok" in page


def test_contact_form_shows_confirmation(client: FlaskClient) -> None:
    response = client.post(
        "/contact",
        data={"name": "N", "email": "n@example.com", "phone": "1", "message": "hi"},
        follow_redirects=True,
    )
    assert b"Your message was sent" in response.data


def test_static_pages_render(client: FlaskClient) -> None:
    assert client.get("/about").status_code == 200
    assert client.get("/contact").status_code == 200
    assert client.get("/login").status_code == 200
    assert client.get("/register").status_code == 200


def test_sanitizer_removes_script_with_content() -> None:
    assert sanitize_html("<p>a</p><script>alert(1)</script>") == "<p>a</p>"


def test_sanitizer_removes_event_handlers_and_javascript_urls() -> None:
    cleaned = sanitize_html('<a href="javascript:evil()" onclick="x()">l</a><img src="http://i/x.png" onerror="y()">')
    assert "javascript" not in cleaned and "onclick" not in cleaned and "onerror" not in cleaned
    assert 'src="http://i/x.png"' in cleaned


def test_sanitizer_keeps_allowed_formatting_and_escapes_text() -> None:
    assert sanitize_html("<strong>b</strong> 1 < 2") == "<strong>b</strong> 1 &lt; 2"


def test_sanitizer_drops_unknown_tags_but_keeps_their_text() -> None:
    assert sanitize_html("<blink>hi</blink>") == "hi"
