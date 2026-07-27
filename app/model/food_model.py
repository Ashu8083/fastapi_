from datetime import datetime,date, time 
from app.db.database import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Integer,String,Date

class Food(Base):
    __tablename__ = "food"

    id : Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )
    name : Mapped[str] = mapped_column(
        String, unique=True
    )
    price : Mapped[int] = mapped_column(
        Integer
    )
    created_at : Mapped[datetime] = mapped_column(
        Date, default=datetime.now
    )