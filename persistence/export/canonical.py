import json
from typing import Any

def canonical_dumps(obj: Any) -> str:
    """
    Deterministic JSON serialization.
    Sorted keys. No extra whitespace.
    UTF-8 normalized.
    Matches Sentinel v0 canonical rules.
    """
    return json.dumps(
        obj,
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    )
