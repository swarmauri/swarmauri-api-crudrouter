from sqlalchemy import Column, ForeignKey, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class UserModel(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, unique=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)
    email_validated = Column(Boolean, default=False)
    active = Column(Boolean, default=True)
    temporary_password = Column(Boolean, default=False)
    date_registered = Column(DateTime, default=datetime.utcnow)
    last_modified = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)