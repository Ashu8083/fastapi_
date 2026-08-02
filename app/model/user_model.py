from datetime import datetime,date, time 
from app.db.database import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Integer,String,Date
from datetime import datetime
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
        __tablename__ = "users"

        id: Mapped[int] = mapped_column(
            Integer, primary_key=True, index=True
        )

        username: Mapped[str] = mapped_column(
            String(220), unique=True, nullable=False
        )

        email: Mapped[str] = mapped_column(
            String(255), unique=True, index=True, nullable=False
        )

        age: Mapped[int] = mapped_column(
            Integer, nullable=False
        )

        created_at: Mapped[datetime] = mapped_column(
            DateTime, default=datetime.now )