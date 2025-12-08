from typing import Generic, TypeVar

from pydantic.generics import GenericModel


T = TypeVar("T")


class ResponseDto(GenericModel, Generic[T]):
    model_config = {"arbitrary_types_allowed": True}

    success: bool = True
    result: T | None = None
    message: str | None = None
