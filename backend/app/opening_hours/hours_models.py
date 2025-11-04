from sqlalchemy import Column, Integer, String, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class OpeningHours(Base):
    __tablename__ = "opening_hours"

    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=False)
    day_of_week = Column(Integer, nullable=False)  # 1=Monday, 7=Sunday
    opening_time = Column(Time, nullable=False)
    closing_time = Column(Time, nullable=False)

    location = relationship("Location", back_populates="opening_hours")
