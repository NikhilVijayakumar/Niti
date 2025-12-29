from typing import List
from pydantic import BaseModel
from src.bavans.akashvani.bala.kadha.application.domain.idea.generate_fantasy.model.metaphor import Metaphor
from src.bavans.akashvani.bala.kadha.application.domain.idea.generate_fantasy.model.narrative_act import NarrativeAct

class FantasyBlueprint(BaseModel):
    metaphor_matrix: List[Metaphor]
    narrative_arc: List[NarrativeAct]
