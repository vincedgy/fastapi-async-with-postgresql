import sqlalchemy
from sqlalchemy import MetaData, func, text
from sqlalchemy.engine import Engine

from lib.db_utils import db_url
from lib.utils import get_logger

logging = get_logger(name='schema')

metadata: MetaData = sqlalchemy.MetaData()

logging.info("Defining table 'notes'")
notes: sqlalchemy.sql.schema.Table = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime(), server_default=text('NOW()')),
    sqlalchemy.Column("text", sqlalchemy.String(length=100)),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)

logging.info("Creating schema")

engine: Engine = sqlalchemy.create_engine(db_url, pool_size=3, max_overflow=0, echo=True)
metadata.create_all(engine)

