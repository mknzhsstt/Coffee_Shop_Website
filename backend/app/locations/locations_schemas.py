from pydantic import BaseModel, EmailStr
from typing import Optional


class LocationBase(BaseModel):
    name: str
    address: str
    phone: Optional[str] = None
    email: Optional[EmailStr] = None


class LocationCreate(LocationBase):
    pass


class LocationUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None


class Location(LocationBase):
    id: int

    class Config:
        from_attributes = True
