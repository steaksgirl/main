from fastapi import APIRouter, HTTPException, Request
from claims_rag.domain.claim import Claim
from claims_rag.generation.response import ClaimAnalysis

router = APIRouter(prefix="/claims", tags=["claims"])


@router.post("", response_model=Claim)
def create_claim(claim: Claim, request: Request) -> Claim:
    return request.app.state.claims.save(claim)


@router.get("/{claim_id}", response_model=Claim)
def get_claim(claim_id: str, request: Request) -> Claim:
    claim = request.app.state.claims.get(claim_id)
    if claim is None:
        raise HTTPException(status_code=404, detail="Claim not found")
    return claim


@router.post("/{claim_id}/analysis", response_model=ClaimAnalysis)
def analyze_claim(claim_id: str, request: Request) -> ClaimAnalysis:
    claim = request.app.state.claims.get(claim_id)
    if claim is None:
        raise HTTPException(status_code=404, detail="Claim not found")
    return request.app.state.analysis.analyze(claim)
