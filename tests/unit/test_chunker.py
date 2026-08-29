from pathlib import Path
from claims_rag.domain.document import Document
from claims_rag.ingestion.chunker import chunk_document


def test_chunker_preserves_content() -> None:
    document = Document(document_id="d", source_path=Path("d.txt"), content="abcdef", category="policies")
    assert [c.text for c in chunk_document(document, size=4, overlap=1)] == ["abcd", "def"]
