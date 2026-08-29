from pathlib import Path
from claims_rag.ingestion.metadata import extract_metadata


def test_metadata_uses_file_and_parent() -> None:
    assert extract_metadata(Path("data/policies/example.txt")) == {"filename": "example.txt", "category": "policies"}
