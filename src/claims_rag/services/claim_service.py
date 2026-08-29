from claims_rag.domain.claim import Claim


class ClaimService:
    def __init__(self) -> None:
        self._claims: dict[str, Claim] = {}

    def save(self, claim: Claim) -> Claim:
        self._claims[claim.claim_id] = claim
        return claim

    def get(self, claim_id: str) -> Claim | None:
        return self._claims.get(claim_id)
