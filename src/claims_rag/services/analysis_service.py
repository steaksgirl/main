from claims_rag.domain.claim import Claim
from claims_rag.generation.llm import grounded_summary
from claims_rag.generation.response import ClaimAnalysis, SourceReference
from claims_rag.retrieval.retriever import Retriever


class AnalysisService:
    def __init__(self, retriever: Retriever) -> None:
        self.retriever = retriever

    def analyze(self, claim: Claim, limit: int = 5) -> ClaimAnalysis:
        query = f"{claim.loss_type} {claim.description}"
        chunks = self.retriever.retrieve(query, limit)
        return ClaimAnalysis(
            claim_id=claim.claim_id,
            summary=grounded_summary(claim.description, chunks),
            sources=[SourceReference(document_id=c.document_id, chunk_id=c.chunk_id, category=c.category, excerpt=c.text[:400]) for c in chunks],
        )
