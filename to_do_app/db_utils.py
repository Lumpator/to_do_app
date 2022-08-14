from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from secret import user, password


def cr_engine():
    CONNECTION_STRING = f"mysql+mysqlconnector://{user}:{password}@localhost:3306/ToDoDB"
    return create_engine(CONNECTION_STRING)


def cr_session():
    Session = sessionmaker(bind=cr_engine())
    return Session()
