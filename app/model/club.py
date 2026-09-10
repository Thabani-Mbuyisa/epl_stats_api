from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Club(Base):
    __tablename__ = "club"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    short_name: Mapped[str] = mapped_column(String, nullable=True)
    abbr: Mapped[str] = mapped_column(String, nullable=True)
    stadium_name: Mapped[str] = mapped_column(String, nullable=True)
    stadium_city: Mapped[str] = mapped_column(String, nullable=True)
    stadium_country: Mapped[str] = mapped_column(String, nullable=True)
    stadium_capacity: Mapped[int] = mapped_column(Integer, nullable=True)