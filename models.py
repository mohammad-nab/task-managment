from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, func, DateTime
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)
    is_completed: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"Task(id={self.id}, name={self.name})"