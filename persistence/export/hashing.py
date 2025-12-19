import hashlib
from typing import Any
from .canonical import canonical_dumps

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def sha256_obj(obj: Any) -> str:
    """
    Hash canonical JSON representation of object.
    """
    canonical = canonical_dumps(obj).encode("utf-8")
    return sha256_bytes(canonical)

def chain_hash(prev_event_hash: str, current_event: dict) -> str:
    """
    Build hash chain: hash(prev_event_hash + canonical(current_event)).
    """
    data = prev_event_hash.encode("utf-8") + canonical_dumps(current_event).encode("utf-8")
    return sha256_bytes(data)
