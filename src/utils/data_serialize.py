from typing import Any
from base64 import b64encode, b64decode


def encode_data(data: Any) -> str:
    try:
        return str(b64encode(repr(data).encode("utf-8")), "utf-8")
    except Exception:
        raise Exception("Unknown encode format")


def decode_data(data: str):
    try:
        return b64decode(data).decode().replace("'", "").replace('"', "")
    except Exception:
        raise Exception("Unknown decode format")
