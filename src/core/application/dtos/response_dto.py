from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar("T")

@dataclass
class ResponseDto(Generic[T]):
    success: bool
    result: T
    message: str
