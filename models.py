from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class Observation(BaseModel):
    gene_symbol: str
    protein_accession: str
    variant_description: str
    tool_outputs: Dict[str, str] = {}
    step_count: int = 0

class Action(BaseModel):
    tool_name: str = Field(description="Values: 'query_function' or 'submit_classification'")
    label_prediction: Optional[str] = None
    rationale: Optional[str] = None

class Reward(BaseModel):
    score: float
    feedback: str