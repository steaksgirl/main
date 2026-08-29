from datetime import date
from claims_rag.domain.claim import Claim
from claims_rag.services.claim_service import ClaimService


def test_claim_service_round_trip() -> None:
    claim = Claim(claim_id="1", policy_number="P", loss_date=date.today(), loss_type="water", description="pipe", claimed_amount=1)
    service = ClaimService()
    service.save(claim)
    assert service.get("1") == claim
