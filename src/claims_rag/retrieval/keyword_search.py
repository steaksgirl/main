from claims_rag.domain.document import DocumentChunk
from .embeddings import embed

# This is a simple keyword-based (lexical/token-based) scoring function. We will change it
# to a more sophisticated semantic scoring/vector retrieval function, as well as add metadata filtering.
def score(query: str, chunk: DocumentChunk) -> float:
    query_terms, chunk_terms = embed(query), embed(chunk.text)
    return float(sum(min(count, chunk_terms[term]) for term, count in query_terms.items()))
