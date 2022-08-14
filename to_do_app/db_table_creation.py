from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import Column, Integer, BOOLEAN, String
from mysql.connector import Error
from db_utils import cr_engine

Base = declarative_base()
try:
    e = cr_engine()
    if not database_exists(e.url):
        create_database(e.url)


    class Tasks(Base):
        __tablename__ = "tasks"
        id = Column(Integer, primary_key=True, autoincrement=True)
        tasks = Column(String(240), nullable=False)
        done = Column(BOOLEAN)

        def is_task_done(self):
            if self.done:
                return "Done"
            return "Not finished"

        def __str__(self):
            return f"id = {self.id} | {self.is_task_done()} | Task = {self.tasks}"


    Base.metadata.create_all(e)
except Error as err:
    print(err)
