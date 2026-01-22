# scripts/publish_to_redmine.py

import json
import os
from dotenv import load_dotenv

from src.nikhil.niti.manager.infrastructure.redmine.redmine_client import RedmineClient
from src.nikhil.niti.manager.infrastructure.redmine.redmine_publisher import publish_estimation_to_redmine

load_dotenv()

REDMINE_URL = os.getenv("REDMINE_BASE_URL")
REDMINE_API_KEY = os.getenv("REDMINE_API_KEY")
PROJECT_ID = os.getenv("REDMINE_PROJECT_ID")

with open("D:/Crew/bala-katha/.Amsha/output/final/output/estimation_architecture/gemini-2.5-flash.json") as f:
    consensus = json.load(f)

client = RedmineClient(REDMINE_URL, REDMINE_API_KEY)

result = publish_estimation_to_redmine(
    consensus_report=consensus,
    redmine=client,
    project_id=PROJECT_ID
)

print(result)
