# infrastructure/trello/trello_publisher.py

from typing import Dict, Any
from .trello_client import TrelloClient
from .trello_card_builder import build_card_name, build_card_description
from .trello_constants import DEFAULT_LISTS


def publish_estimation_to_trello(
    consensus_report: Dict[str, Any],
    trello_client: TrelloClient,
    board_name: str
) -> Dict[str, Any]:
    """
    Publishes CREW-02 estimation JSON to Trello.
    """

    # 1. Create board
    board = trello_client.create_board(board_name)
    board_id = board["id"]

    # 2. Create lists
    lists = {}
    for name in DEFAULT_LISTS:
        lst = trello_client.create_list(board_id, name)
        lists[name] = lst["id"]

    sprint_list_id = lists["Sprint Backlog"]

    # 3. Create cards
    created_cards = []

    for item in consensus_report["consensus_report"]:
        card = trello_client.create_card(
            list_id=sprint_list_id,
            name=build_card_name(item),
            desc=build_card_description(item)
        )

        created_cards.append({
            "story_id": item["story_id"],
            "card_id": card["id"],
            "card_url": card["url"]
        })

    return {
        "board_id": board_id,
        "board_url": board["url"],
        "cards": created_cards
    }
