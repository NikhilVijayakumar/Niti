from typing import List
from pydantic import BaseModel, Field


class SprintAllocation(BaseModel):
    story_id: str = Field(..., description="Story identifier selected for the sprint")
    assignee: str = Field(..., description="Developer assigned to the story")
    estimated_hours: float = Field(..., description="Final estimated hours for this story")


class SprintCapacitySummary(BaseModel):
    developer: str = Field(..., description="Developer name")
    available_hours: float = Field(..., description="Net available hours for the sprint")
    allocated_hours: float = Field(..., description="Total hours allocated in this sprint")
    utilization_percentage: float = Field(
        ..., description="Allocated vs available capacity percentage"
    )


class SprintPlan(BaseModel):
    sprint_metadata: dict = Field(
        ..., description="Sprint identifiers such as sprint number and duration"
    )
    sprint_goal: str = Field(..., description="High-level objective for the sprint")
    allocations: List[SprintAllocation] = Field(
        ..., description="Stories committed to this sprint"
    )
    capacity_summary: List[SprintCapacitySummary] = Field(
        ..., description="Per-developer capacity utilization summary"
    )
