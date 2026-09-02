import re
from collections import Counter # dictionary that tracks how many times each token occurs

def embed(text: str) -> Counter[str]:
    """Dependency-free token representation; swap for an embedding provider in production."""
    return Counter(re.findall(r"[a-z0-9]+", text.lower()))
