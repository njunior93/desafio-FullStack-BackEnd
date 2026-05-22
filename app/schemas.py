from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class VoluntarioCreate(BaseModel):
    name: str
    email: EmailStr
    fone: str
    position: str
    availability: str

class VoluntarioUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    fone: Optional[str] = None
    position: Optional[str] = None
    availability: Optional[str] = None
    status: Optional[bool] = None

class VoluntarioResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    fone: str
    position: str
    availability: str
    status: bool
    data_inscricao: datetime

    class Config: 
        orm_mode = True