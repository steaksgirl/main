from claims_rag.domain.document import DocumentChunk


def grounded_summary(claim_description: str, sources: list[DocumentChunk]) -> str:
    if not sources:
        return "No relevant policy source was found. Escalate for manual review."
    excerpts = " ".join(source.text[:220].replace("\n", " ") for source in sources[:2])
    return f"Based on the retrieved policy material, review the claim against these provisions: {excerpts}"
