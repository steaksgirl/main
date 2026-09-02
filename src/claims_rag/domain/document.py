from pathlib import Path
from pydantic import BaseModel, Field


class Document(BaseModel):
    document_id: str
    source_path: Path
    content: str
    category: str
    metadata: dict[str, str] = Field(default_factory=dict) # Metadata gives the evidence context


class DocumentChunk(BaseModel):
    chunk_id: str
    document_id: str
    text: str
    category: str
    metadata: dict[str, str] = Field(default_factory=dict)
