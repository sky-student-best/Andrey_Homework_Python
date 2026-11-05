import uuid


def test_get_project_positive(api, project):
    """Позитивный: существующий проект возвращается со статусом 200."""
    title = f"get-{uuid.uuid4().hex[:8]}"
    api.update_project(project, {"title": title})

    response = api.get_project(project)

    assert response.status_code == 200, response.text
    body = response.json()
    assert body["id"] == project
    assert body["title"] == title


def test_get_project_negative_unknown_id(api):
    """Негативный: несуществующий id — 404."""
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = api.get_project(fake_id)

    assert response.status_code == 404, response.text
