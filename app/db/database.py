from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql://root:root1234@localhost:3306/zomato_clone"

engine = create_engine(DATABASE_URL,
                       pool_pre_ping=True)

SessionLocal= sessionmaker(autocommit=False,
                            autoflush=False, 
                            bind=engine
                            )

Base = declarative_base() # to register the models with the database 
                        #(which tell sqlalchemy that these are the models that we want to create in the database)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

