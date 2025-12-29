from pydantic import BaseModel

class Metaphor(BaseModel):
    scientific_concept: str
    functional_role: str
    fantasy_translation: str
