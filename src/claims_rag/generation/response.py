from pydantic import BaseModel


class SourceReference(BaseModel):
    document_id: str
    chunk_id: str
    category: str
    excerpt: str


class ClaimAnalysis(BaseModel):
    claim_id: str
    summary: str
    sources: list[SourceReference]
    disclaimer: str = "This is decision support only and does not determine coverage."
