from datetime import datetime,date, time 
from app.db.database import Base
from sqlalchemy.orm import Mapped,mapped_column, relationship
from sqlalchemy import ForeignKey, Integer,String,Date
from sqlalchemy import Enum as SqlEnum
from app.enums.food_type import FOODTYPE
from enum import Enum

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
    # category : Mapped[CategoryEnum] = mapped_column(
    #     SqlEnum(CategoryEnum)
        
    # )
    food_type :Mapped[FOODTYPE] = mapped_column(
        SqlEnum(FOODTYPE)
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
                            )
    

