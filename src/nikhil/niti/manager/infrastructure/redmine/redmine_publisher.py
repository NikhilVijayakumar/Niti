from typing import Dict, Any
from .redmine_client import RedmineClient
from .redmine_issue_builder import build_story_issue, build_task_issue


def publish_estimation_to_redmine(
    consensus_report: Dict[str, Any],
    redmine: RedmineClient,
    project_id: str
) -> Dict[str, Any]:

    created = []

    for item in consensus_report["consensus_report"]:
        # 1. Create Story
        story_payload = build_story_issue(item, project_id)
        story_response = redmine.create_issue(story_payload)
        story_id = story_response["issue"]["id"]

        # 2. Create Task (child)
        task_payload = build_task_issue(item, project_id, parent_id=story_id)
        task_response = redmine.create_issue(task_payload)

        created.append({
            "story_key": item["story_id"],
            "story_issue_id": story_id,
            "task_issue_id": task_response["issue"]["id"]
        })

    return {
        "project_id": project_id,
        "created_issues": created
    }
