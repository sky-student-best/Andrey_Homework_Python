import uuid


def test_update_project_positive(api, project):
    """Позитивный: переименование проходит, данные обновляются."""
    new_title = f"updated-{uuid.uuid4().hex[:8]}"
    response = api.update_project(project, {"title": new_title})

    assert response.status_code == 200, response.text

    check = api.get_project(project)
    assert check.status_code == 200, check.text
    assert check.json()["title"] == new_title


def test_update_project_negative_unknown_id(api):
    """Негативный: обновление несуществующего проекта — 404."""
    fake_id = "00000000-0000-0000-0000-000000000000"
    payload = {"title": f"neg-{uuid.uuid4().hex[:8]}"}
    response = api.update_project(fake_id, payload)

    assert response.status_code == 404, response.text
