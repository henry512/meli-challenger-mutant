from typing import Any
from base64 import b64encode


def serialize_data(data: Any) -> str:
    try:
        return str(b64encode(repr(data).encode("utf-8")), "utf-8")
    except Exception:
        raise Exception("Unknown serialization format")
