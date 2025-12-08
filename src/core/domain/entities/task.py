from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from src.infrastructure.persistence.data.base import Base


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("project.id"), index=True)
    title = Column(String(255), nullable=False)
    description = Column(String, nullable=True)
    due_date = Column(DateTime(timezone=True), nullable=True)
    status = Column(String(20), default="todo", nullable=False)
    closed_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
