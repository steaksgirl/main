from pathlib import Path
from claims_rag.domain.document import Document


def load_documents(data_dir: Path) -> list[Document]:
    documents: list[Document] = []
    for path in data_dir.glob("**/*.txt"):
        category = path.parent.name
        documents.append(Document(document_id=path.stem, source_path=path, content=path.read_text(encoding="utf-8"), category=category))
    return documents
