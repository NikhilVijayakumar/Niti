import requests
from typing import Dict, Any


class RedmineClient:

    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key

    def _headers(self) -> Dict[str, str]:
        return {
            "X-Redmine-API-Key": self.api_key,
            "Content-Type": "application/json"
        }

    def create_issue(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        response = requests.post(
            f"{self.base_url}/issues.json",
            headers=self._headers(),
            json={"issue": payload},
            timeout=30
        )
        response.raise_for_status()
        return response.json()
