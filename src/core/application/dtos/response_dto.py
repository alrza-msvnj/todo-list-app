from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar("T")

@dataclass
class ResponseDto(Generic[T]):
    success: bool
    result: T | None
    message: str | None

    def __init__(self, result: T | None = None, success: bool = True, message: str | None = None):
        self.success = success
        self.result = result
        self.message = message
