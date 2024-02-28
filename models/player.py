from sqlalchemy import JSON, Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from core.database import Base


class Player(Base):
    __tablename__ = "players"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    disclaimer: Mapped[str] = mapped_column(String)
    ranking: Mapped[int] = mapped_column(Integer)
    profilepicurl: Mapped[str] = mapped_column(String)
    goat: Mapped[bool] = mapped_column(Boolean)
    votes: Mapped[list[int]] = mapped_column(JSON, default=set)
