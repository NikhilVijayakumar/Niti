# infrastructure/trello/trello_client.py

import requests
from typing import Dict, Any
from .trello_constants import TRELLO_BASE_URL


class TrelloClient:

    def __init__(self, api_key: str, token: str):
        self.api_key = api_key
        self.token = token

    def _auth(self) -> Dict[str, str]:
        return {"key": self.api_key, "token": self.token}

    def create_board(self, name: str) -> Dict[str, Any]:
        res = requests.post(
            f"{TRELLO_BASE_URL}/boards",
            data={"name": name, "defaultLists": "false", **self._auth()},
            timeout=30
        )
        res.raise_for_status()
        return res.json()

    def create_list(self, board_id: str, name: str) -> Dict[str, Any]:
        res = requests.post(
            f"{TRELLO_BASE_URL}/lists",
            data={"idBoard": board_id, "name": name, **self._auth()},
            timeout=30
        )
        res.raise_for_status()
        return res.json()

    def create_card(self, list_id: str, name: str, desc: str) -> Dict[str, Any]:
        res = requests.post(
            f"{TRELLO_BASE_URL}/cards",
            data={"idList": list_id, "name": name, "desc": desc, **self._auth()},
            timeout=30
        )
        res.raise_for_status()
        return res.json()
