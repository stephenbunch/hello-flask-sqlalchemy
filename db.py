import os
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, Boolean, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()
db = create_engine(os.environ["DATABASE_URL"])
Base = declarative_base()


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    description = Column(String(80), nullable=False, default="")
    completed = Column(Boolean, nullable=False, default=False)


if __name__ == "__main__":
    Base.metadata.create_all(db)
