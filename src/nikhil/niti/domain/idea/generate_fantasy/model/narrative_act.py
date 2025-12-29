from pydantic import BaseModel

class NarrativeAct(BaseModel):
    act_title: str
    description: str
    scientific_stage_mapping: str
