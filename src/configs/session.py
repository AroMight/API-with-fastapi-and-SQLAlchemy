from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///./test.db", echo=True)

session = sessionmaker(bind=engine)

Session = session()


