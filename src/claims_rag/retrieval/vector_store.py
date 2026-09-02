from claims_rag.domain.document import DocumentChunk
from .keyword_search import score


class InMemoryVectorStore:
    def __init__(self) -> None:
        self.chunks: list[DocumentChunk] = []

    def add(self, chunks: list[DocumentChunk]) -> None:
        self.chunks.extend(chunks)

    def search(self, query: str, limit: int = 5) -> list[DocumentChunk]:
        ranked = sorted(
            self.chunks, 
            key=lambda chunk: score(query, chunk), 
            reverse=True
        )
        return [chunk for chunk in ranked[:limit] if score(query, chunk) > 0]
