from pathlib import Path
from claims_rag.ingestion.chunker import chunk_document
from claims_rag.ingestion.loader import load_documents
from claims_rag.domain.document import DocumentChunk
from .vector_store import InMemoryVectorStore


class Retriever:
    def __init__(self, store: InMemoryVectorStore | None = None) -> None:
        self.store = store or InMemoryVectorStore()

    # Our ingestion pipeline:
    def index_directory(self, data_dir: Path) -> int:
        chunks = [chunk for document in load_documents(data_dir) for chunk in chunk_document(document)]
        self.store.add(chunks) # Add the chunks to the vector store
        return len(chunks)

    def retrieve(self, query: str, limit: int = 5) -> list[DocumentChunk]:
        return self.store.search(query, limit)
