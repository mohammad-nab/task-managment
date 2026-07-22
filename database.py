from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///tasks.db", echo=True)

SessionLocal = sessionmaker(bind=engine)
