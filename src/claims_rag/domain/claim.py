from datetime import date
from pydantic import BaseModel, Field


class Claim(BaseModel):
    claim_id: str
    policy_number: str
    loss_date: date
    loss_type: str
    description: str
    claimed_amount: float = Field(ge=0)
    state: str | None = None
