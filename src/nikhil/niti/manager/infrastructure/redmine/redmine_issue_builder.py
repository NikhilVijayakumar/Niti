from .redmine_constants import RISK_TO_PRIORITY


def build_story_issue(item: dict, project_id: str) -> dict:
    return {
        "project_id": project_id,
        "tracker_id": 19,  # Story
        "priority_id": RISK_TO_PRIORITY.get(item["risk_level"], 4),
        "subject": f"{item['story_id']} – {item['system_component']}",
        "description": f"""
Story ID: {item['story_id']}

Component:
{item['system_component']}

Estimation:
- Base: {item['base_estimate_hours']} hrs
- TCF: {item['tcf']}
- AEF: {item['aef']}
- Final: {item['final_estimate_hours']} hrs

Risk:
{item['risk_level']}

Justification:
{item['justification']}
""".strip(),
        "estimated_hours": item["final_estimate_hours"]
    }


def build_task_issue(item: dict, project_id: str, parent_id: int) -> dict:
    return {
        "project_id": project_id,
        "tracker_id": 9,  # Task
        "priority_id": RISK_TO_PRIORITY.get(item["risk_level"], 4),
        "parent_issue_id": parent_id,
        "subject": f"Implement {item['system_component']}",
        "description": "Implementation task generated from approved estimation.",
        "estimated_hours": item["final_estimate_hours"]
    }
