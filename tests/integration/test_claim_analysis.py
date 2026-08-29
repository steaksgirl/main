from datetime import date
from pathlib import Path
from claims_rag.domain.claim import Claim
from claims_rag.domain.document import DocumentChunk
from claims_rag.retrieval.retriever import Retriever
from claims_rag.services.analysis_service import AnalysisService


def test_analysis_includes_source() -> None:
    retriever = Retriever()
    retriever.store.add([DocumentChunk(chunk_id="p:0", document_id="policy", text="Pipe loss is covered.", category="policies")])
    claim = Claim(claim_id="1", policy_number="P", loss_date=date.today(), loss_type="pipe", description="pipe loss", claimed_amount=1)
    result = AnalysisService(retriever).analyze(claim)
    assert result.sources[0].document_id == "policy"
