from typing import List
from pydantic import BaseModel, Field


class ProductBacklogItem(BaseModel):
    story_id: str = Field(..., description="Unique identifier for the story")
    epic: str = Field(..., description="Epic this story belongs to")
    title: str = Field(..., description="User-facing value proposition")
    business_value: str = Field(..., description="High | Medium | Low")
    brd_reference: str = Field(..., description="Reference to BRD section")


class ProductBacklog(BaseModel):
    product_backlog: List[ProductBacklogItem] = Field(
        ..., description="Complete prioritized product backlog"
    )
