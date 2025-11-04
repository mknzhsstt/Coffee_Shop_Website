from sqlalchemy.orm import Session
from app.opening_hours.hours_models import OpeningHours
from app.opening_hours import hours_schemas


def get_opening_hours_by_id(db: Session, hours_id: int):
    return db.query(OpeningHours).filter(OpeningHours.id == hours_id).first()


def get_opening_hours(db: Session, skip: int = 0, limit: int = 100):
    return db.query(OpeningHours).offset(skip).limit(limit).all()


def get_opening_hours_by_location(db: Session, location_id: int):
    return db.query(OpeningHours).filter(OpeningHours.location_id == location_id).all()


def create_opening_hours(db: Session, hours: hours_schemas.OpeningHoursCreate):
    db_hours = OpeningHours(**hours.dict())
    db.add(db_hours)
    db.commit()
    db.refresh(db_hours)
    return db_hours


def update_opening_hours(
    db: Session, hours_id: int, hours: hours_schemas.OpeningHoursUpdate
):
    db_hours = db.query(OpeningHours).filter(OpeningHours.id == hours_id).first()
    if db_hours:
        update_data = hours.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_hours, key, value)
        db.commit()
        db.refresh(db_hours)
    return db_hours


def delete_opening_hours(db: Session, hours_id: int):
    db_hours = db.query(OpeningHours).filter(OpeningHours.id == hours_id).first()
    if db_hours:
        db.delete(db_hours)
        db.commit()
    return db_hours
