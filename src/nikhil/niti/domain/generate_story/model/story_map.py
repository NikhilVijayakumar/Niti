from typing import List
from pydantic import BaseModel, Field

class StoryItem(BaseModel):
    story_id: str = Field(..., description="Unique identifier for the story (e.g., US-001)")
    epic: str = Field(..., description="The epic this story belongs to")
    title: str = Field(..., description="Value Proposition Title")
    brd_reference: str = Field(..., description="Reference to the BRD section")

class StoryMap(BaseModel):
    story_map: List[StoryItem] = Field(..., description="List of stories in the map")
