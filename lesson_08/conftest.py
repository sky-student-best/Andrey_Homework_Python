import os
import uuid

import pytest

from yougile_api import ProjectsApi

BASE_URL = "https://ru.yougile.com/api-v2"


@pytest.fixture
def token() -> str:
    """Токен берём из переменной окружения, а не из кода."""
    value = os.environ.get("YOUGILE_TOKEN", "ID0-sB5sGHBYzJIe3e2pt1ys6aqFkW6djmcnUWqqPfj_wJqiruAbMSERjqCVOTeI")
    if not value:
        pytest.skip("Переменная окружения YOUGILE_TOKEN не задана")
    return value


@pytest.fixture
def api(token) -> ProjectsApi:
    return ProjectsApi(token=token)


@pytest.fixture
def project(api) -> str:
    """Создаёт проект с уникальным именем и удаляет его после теста."""
    payload = {"title": f"autotest-{uuid.uuid4().hex[:8]}"}
    response = api.create_project(payload)
    project_id = response.json()["id"]

    yield project_id

    api.update_project(project_id, {"deleted": True})
