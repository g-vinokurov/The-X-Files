
import sqlalchemy
import sqlalchemy.orm as orm

from Storage import Models

from Config import DB_URL
from Config import DB_ECHO


class Database:
    def __init__(self, url, echo):
        engine = sqlalchemy.create_engine(url=url, echo=echo)
        self.Session = orm.sessionmaker(bind=engine)
        Models.Base.metadata.create_all(engine)


db = Database(url=DB_URL, echo=DB_ECHO)
