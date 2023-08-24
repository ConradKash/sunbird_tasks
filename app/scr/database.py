import sqlalchemy as _sql
from sqlalchemy.orm import declarative_base
import sqlalchemy.orm as _orm

SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

engine = _sql.create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"chech_sum_thread": False} 
)

sessionLocal = _orm.sessionmaker(autocommit = False, autoflush= False, bind=engine)

Base = declarative_base()