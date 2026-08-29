from contextlib import asynccontextmanager
from fastapi import FastAPI
from claims_rag.api import claims, health
from claims_rag.config import settings
from claims_rag.logging_config import configure_logging
from claims_rag.retrieval.retriever import Retriever
from claims_rag.services.analysis_service import AnalysisService
from claims_rag.services.claim_service import ClaimService


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    retriever = Retriever()
    retriever.index_directory(settings.data_dir)
    app.state.claims = ClaimService()
    app.state.analysis = AnalysisService(retriever)
    yield


app = FastAPI(title=settings.app_name, version="0.1.0", lifespan=lifespan)
app.include_router(health.router)
app.include_router(claims.router)
