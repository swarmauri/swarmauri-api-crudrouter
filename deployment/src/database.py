from sqlalchemy import create_engine, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

SQL_DB_FILENAME = os.getenv("SQL_DB_FILENAME")

if SQL_DB_FILENAME:
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{SQL_DB_FILENAME}"
    print(f"Database will be located at: {os.path.abspath(SQL_DB_FILENAME)}")
else:
   
    SQLALCHEMY_DATABASE_URL = "sqlite:////app/db/app.db"  
    print('Creating new db @', SQLALCHEMY_DATABASE_URL)
db_directory = os.path.dirname(SQL_DB_FILENAME) if SQL_DB_FILENAME else "/app/db/"
os.makedirs(db_directory, exist_ok=True) 

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)

Base = declarative_base()

event.listen(engine, 'connect', lambda c, _: c.execute('pragma foreign_keys=on'))