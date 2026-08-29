from pathlib import Path


def extract_metadata(path: Path) -> dict[str, str]:
    return {"filename": path.name, "category": path.parent.name}
