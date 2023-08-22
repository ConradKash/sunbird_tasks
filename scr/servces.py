import database as _database

def create_database():
    return _database.Base.meta.create_all(bind=_database.engine)