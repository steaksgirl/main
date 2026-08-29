SYSTEM_PROMPT = "You are a careful claims assistant. Use only supplied sources and flag uncertainty."


def build_claim_prompt(claim_description: str, context: str) -> str:
    return f"{SYSTEM_PROMPT}\n\nClaim: {claim_description}\n\nSources:\n{context}"
