import requests

BASE_URL = "https://ru.yougile.com/api-v2"


class ProjectsApi:
    """Обёртка над методами проектов (аналог Page Object для API)."""

    def __init__(self, token: str = "", base_url: str = BASE_URL):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def create_project(self, payload: dict) -> requests.Response:
        url = f"{self.base_url}/projects"
        return requests.post(url, json=payload, headers=self.headers)

    def get_project(self, project_id: str) -> requests.Response:
        url = f"{self.base_url}/projects/{project_id}"
        return requests.get(url, headers=self.headers)

    def update_project(
        self, project_id: str, payload: dict
    ) -> requests.Response:
        url = f"{self.base_url}/projects/{project_id}"
        return requests.put(url, json=payload, headers=self.headers)
