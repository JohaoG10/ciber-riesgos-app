# modules/db.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONN_STR = (
    "mssql+pyodbc://@localhost/CiberRiesgosDB"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine       = create_engine(CONN_STR, echo=False)
SessionLocal = sessionmaker(bind=engine)
Base         = declarative_base()
