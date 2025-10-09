from dataclasses import dataclass
from typing import TypeVar


T = TypeVar

@dataclass
class ResponseDto:
    success: bool
    result: T
    message: str
