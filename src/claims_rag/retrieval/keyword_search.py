from claims_rag.domain.document import DocumentChunk
from .embeddings import embed


def score(query: str, chunk: DocumentChunk) -> float:
    query_terms, chunk_terms = embed(query), embed(chunk.text)
    return float(sum(min(count, chunk_terms[term]) for term, count in query_terms.items()))
