from claims_rag.domain.document import Document, DocumentChunk


def chunk_document(document: Document, size: int = 800, overlap: int = 120) -> list[DocumentChunk]:
    if size <= overlap:
        raise ValueError("size must be greater than overlap")
    text, chunks, start = document.content.strip(), [], 0
    while start < len(text):
        end = min(len(text), start + size)
        chunks.append(DocumentChunk(chunk_id=f"{document.document_id}:{len(chunks)}", document_id=document.document_id, text=text[start:end], category=document.category, metadata=document.metadata))
        start += size - overlap
    return chunks
