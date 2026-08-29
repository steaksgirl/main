from pydantic import BaseModel


class CoverageFinding(BaseModel):
    coverage: str
    status: str
    rationale: str
