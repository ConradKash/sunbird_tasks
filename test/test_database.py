import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from app.scr import services as _services
from app.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

engine = _sql.create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()
        

app.dependency_overrides[_services.get_db] = override_get_db
