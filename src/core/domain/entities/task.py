from dataclasses import dataclass
from datetime import date, datetime, timezone
from typing import Literal

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.persistence.data.base import Base


TaskStatus = Literal["todo", "doing", "done"]


@dataclass
class Task(Base):
    __tablename__ = 'task'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        init=False
    )

    project_id: Mapped[int] = mapped_column(
        ForeignKey("project.id"),
        index=True
    )
    
    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )

    due_date: Mapped[date | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    status: Mapped[TaskStatus] = mapped_column(
        String(20),
        default="todo",
        nullable=False
    )

    creation_timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default_factory=lambda: datetime.now(timezone.utc),
        init=False
    )
