from app.scr import database as _database, model as _model, schemas as _schemas
import sqlalchemy.orm as _orm
from sqlalchemy import select
from app.scr.model import language_id

def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.sessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def get_predicts(db: _orm.Session):
    predicts = select(language_id)
    return db.execute(predicts).scalars().all()
        
def send_report(db: _orm.Session, prediction: _schemas.predictout):
    db_predict = _model.language_id(text=prediction.text, language=prediction.language, process_time=prediction.process_time)
    db.add(db_predict)
    db.commit()
    db.refresh(db_predict)
    return db_predict