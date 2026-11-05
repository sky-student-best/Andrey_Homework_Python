import uuid


def test_create_project_positive(api):
    """Позитивный: проект создаётся, статус 201, возвращается id."""
    payload = {"title": f"create-{uuid.uuid4().hex[:8]}"}
    response = api.create_project(payload)

    assert response.status_code == 201, response.text
    body = response.json()
    assert "id" in body


def test_create_project_negative_no_title(api):
    """Негативный: без title запрос отклоняется с 400."""
    payload = {"invalid_field": "some value"}
    response = api.create_project(payload)

    assert response.status_code == 400, response.text


def test_create_project_negative_no_auth(api):
    """Негативный: без токена — 401."""
    api.headers["Authorization"] = "Bearer "
    payload = {"title": f"noauth-{uuid.uuid4().hex[:8]}"}
    response = api.create_project(payload)

    assert response.status_code == 401, response.text
