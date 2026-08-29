# Claims RAG Assistant

A lightweight, source-grounded starter application for analyzing insurance claims against policy documents, endorsements, and procedures.

## Quick start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
python scripts/create_sample_claims.py
python scripts/ingest_documents.py
uvicorn claims_rag.main:app --reload
```

Open the API documentation at `http://127.0.0.1:8000/docs`, or run the UI:

```powershell
streamlit run ui/streamlit_app.py
```

## Design

The default retrieval implementation is an in-memory lexical search so the project works without external services. Replace `retrieval/embeddings.py` and `retrieval/vector_store.py` with your preferred embedding model and vector database when ready.

Environment variables are documented in `.env.example`.
