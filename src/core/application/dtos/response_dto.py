from typing import Generic, TypeVar

from pydantic.generics import GenericModel


T = TypeVar("T")


class ResponseDto(GenericModel, Generic[T]):
    success: bool
    result: T | None
    message: str | None
