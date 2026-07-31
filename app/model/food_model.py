from datetime import datetime,date, time 
from app.db.database import Base
from sqlalchemy.orm import Mapped,mapped_column, relationship
from sqlalchemy import ForeignKey, Integer,String,Date

class Food(Base):
    __tablename__ = "food"

    id : Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )
    name : Mapped[str] = mapped_column(
        String(255), unique=True
    )
    price : Mapped[int] = mapped_column(
        Integer
    )
    category : Mapped[str] = mapped_column(
        String(255)
    )
    restaurant_id : Mapped[int] = mapped_column(
        ForeignKey("restaurant.id"), index=True
    )
    created_at : Mapped[datetime] = mapped_column(
        Date, default=datetime.now
    )

    restaurant  = relationship(
                            "Restaurant",
                            back_populates="food",
                            cascade="all, delete-orphan")
    

