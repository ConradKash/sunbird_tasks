from app.scr import database as _database, model as _model, schemas as _schemas
import sqlalchemy.orm as _orm

def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.sessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def send_report(db: _orm.Session, prediction: _schemas.PredictBase):
    db_predict = _model.language_id(text=prediction.text, language=prediction.language, process_time=prediction.process_time)
    db.add(db_predict)
    db.commit()
    db.refresh(db_predict)
    return db_predict