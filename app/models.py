from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime
from .database import Base
from datetime import datetime
from typing import Optional

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str]
    phone: Mapped[Optional[str]] = mapped_column(nullable=True)
    name: Mapped[Optional[str]] = mapped_column(nullable=True)
    role: Mapped[str] = mapped_column(default="user")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),default=datetime.utcnow,nullable=False)


class Ad(Base):
    __tablename__ = "ads"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column()

    status: Mapped[int] = mapped_column()
    type: Mapped[int] = mapped_column()
    breed: Mapped[int] = mapped_column()
    color: Mapped[int] = mapped_column()
    size: Mapped[int] = mapped_column()
    distincs: Mapped[Optional[int]] = mapped_column(nullable=True)
    nickname: Mapped[Optional[int]] = mapped_column(nullable=True)
    danger: Mapped[int] = mapped_column()
    location: Mapped[int] = mapped_column()
    geoLocation: Mapped[int] = mapped_column()
    time: Mapped[int] = mapped_column()

    contactName: Mapped[str]
    contactPhone: Mapped[str]
    contactEmail: Mapped[str]
    extras: Mapped[Optional[str]] = mapped_column(nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )


