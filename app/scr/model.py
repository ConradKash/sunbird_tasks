import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
import database as _database

class language_id(_database.base):
    __tablename__ = "Model performance"
    id = _sql.Column(_sql.Integer, primary_key = True, index=True)
    text = _sql.Column(_sql.String, index=True)
    language = _sql.Column(_sql.String, index=True)
    Process_time = _sql.Column(_sql.Float, index=True)