from pydantic import BaseModel
from typing import Optional
from datetime import time


class OpeningHoursBase(BaseModel):
    location_id: int
    day_of_week: int  # 1=Monday, 7=Sunday
    opening_time: time
    closing_time: time


class OpeningHoursCreate(OpeningHoursBase):
    pass


class OpeningHoursUpdate(BaseModel):
    location_id: Optional[int] = None
    day_of_week: Optional[int] = None
    opening_time: Optional[time] = None
    closing_time: Optional[time] = None


class OpeningHours(OpeningHoursBase):
    id: int

    class Config:
        from_attributes = True
