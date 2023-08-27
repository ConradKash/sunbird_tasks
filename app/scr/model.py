import sqlalchemy as _sql
import app.scr.database as _database

class language_id(_database.Base):
    __tablename__ = "Model performance"
    id = _sql.Column(_sql.Integer, primary_key = True, index=True)
    text = _sql.Column(_sql.String, index=True)
    language = _sql.Column(_sql.String, index=True)
    process_time = _sql.Column(_sql.Float, index=True)