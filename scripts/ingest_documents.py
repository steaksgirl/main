from claims_rag.config import settings
from claims_rag.retrieval.retriever import Retriever


if __name__ == "__main__":
    count = Retriever().index_directory(settings.data_dir)
    print(f"Indexed {count} document chunks from {settings.data_dir}.")
