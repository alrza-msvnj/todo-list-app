from dataclasses import dataclass
from datetime import datetime, timezone

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.persistence.data.base import Base


@dataclass
class Project(Base):
    __tablename__ = 'project'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        init=False
    )

    name: Mapped[str] = mapped_column(
        String(255), 
        unique=True, index=True, 
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        String, 
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        init=False
    )
