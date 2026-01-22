# scripts/publish_to_trello.py

import sys
import os
from dotenv import load_dotenv

# Add project root to sys.path to allow imports from src
current_dir = os.path.dirname(os.path.abspath(__file__))
# 4 levels up from src/nikhil/niti/app is src (or rather, Arsha/Niti)
project_root = os.path.abspath(os.path.join(current_dir, "../../../../"))
sys.path.insert(0, project_root)

# Load environment variables from .env file
load_dotenv(os.path.join(project_root, ".env"))

import json
from src.nikhil.niti.manager.infrastructure.trello.trello_client import TrelloClient
from src.nikhil.niti.manager.infrastructure.trello.trello_publisher import publish_estimation_to_trello

TRELLO_API_KEY = os.getenv("TRELLO_API_KEY")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")

# Relative to project root, this is D:/Crew/bala-katha/.Amsha/output/final/output/estimation_architecture/gemini-2.5-flash.json
json_file_path = os.path.join(project_root, "D:/Crew/bala-katha/.Amsha/output/final/output/estimation_architecture/gemini-2.5-flash.json")
# If file doesn't exist, this will fail, but with a clear error.
# For now we use the path derived from the previous windows path if possible, or just a safe guess.
if not os.path.exists(json_file_path):
    # Fallback to check if user meant relative to current dir
    pass

try:
    with open(json_file_path) as f:
        consensus = json.load(f)
except FileNotFoundError:
    print(f"Warning: Consensus file not found at {json_file_path}. Please update the path.")
    consensus = {}

if TRELLO_API_KEY and TRELLO_TOKEN:
    trello = TrelloClient(TRELLO_API_KEY, TRELLO_TOKEN)
else:
    print("Error: TRELLO_API_KEY or TRELLO_TOKEN not found in environment variables.")
    sys.exit(1)

result = publish_estimation_to_trello(
    consensus_report=consensus,
    trello_client=trello,
    board_name="NITI – Sprint Board"
)

print(result)
