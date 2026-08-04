from datetime import datetime,date, time 
from app.db.database import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import Integer,String,Date


class Restaurant(Base):
    __tablename__ = "restaurant"

    id : Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True,autoincrement=True
    )
    email: Mapped[str] = mapped_column(
        String(255),unique=True
    )
    name : Mapped[str] = mapped_column(
        String(255), unique=True
    )
    location : Mapped[str] = mapped_column(
        String(255)
    )
    rating : Mapped[int] = mapped_column(
        Integer,nullable=True
    )
    created_at : Mapped[datetime] = mapped_column(
        Date, default=datetime.now
    )
    updated_at : Mapped[datetime] = mapped_column(
        Date, default=datetime.now, onupdate=datetime.now
    )
    food = relationship(
        "Food", 
        back_populates="restaurant",
        cascade="all, delete-orphan")