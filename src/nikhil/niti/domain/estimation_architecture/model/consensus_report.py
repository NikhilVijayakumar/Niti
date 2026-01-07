from typing import List
from pydantic import BaseModel, Field


class ConsensusItem(BaseModel):
    story_id: str = Field(..., description="Story identifier")
    system_component: str = Field(..., description="Architectural component")
    base_estimate_hours: float = Field(..., description="Senior-level base estimate")
    tcf: float = Field(..., description="Team Competency Factor applied")
    aef: float = Field(..., description="AI Efficiency Factor applied")
    final_estimate_hours: float = Field(..., description="Final adjusted estimate")
    risk_level: str = Field(..., description="Low | Medium | High")
    justification: str = Field(..., description="Explanation of estimate adjustments")


class ConsensusReport(BaseModel):
    consensus_report: List[ConsensusItem] = Field(
        ..., description="Final estimation and architecture consensus"
    )
