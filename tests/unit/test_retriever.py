from pathlib import Path
from claims_rag.domain.document import DocumentChunk
from claims_rag.retrieval.retriever import Retriever


def test_retriever_returns_relevant_chunk() -> None:
    retriever = Retriever()
    retriever.store.add([DocumentChunk(chunk_id="1", document_id="policy", text="Sudden pipe discharge is covered.", category="policies")])
    assert retriever.retrieve("pipe discharge")[0].document_id == "policy"
