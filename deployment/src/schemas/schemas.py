from datetime import datetime, date
from uuid import UUID
from typing import Union, List, Any, ForwardRef, Optional
import base64
from pydantic import BaseModel, validator, Field, ConfigDict
from fastapi import UploadFile, File
from typing import ForwardRef

class UserUpdate(BaseModel):
    email: str
    password: str
    email_validated: bool = False
    active: bool = True
    temporary_password: bool = False
    last_modified: datetime = datetime.utcnow()

class UserCreate(UserUpdate):
    id: str

class User(UserCreate):
    date_registered: datetime
    model_config = ConfigDict(from_attributes=True)