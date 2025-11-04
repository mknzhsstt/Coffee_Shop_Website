from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.opening_hours import hours_schemas, hours_db

router = APIRouter()


@router.get("/", response_model=List[hours_schemas.OpeningHours])
def read_opening_hours(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    hours = hours_db.get_opening_hours(db, skip=skip, limit=limit)
    return hours


@router.post("/", response_model=hours_schemas.OpeningHours)
def create_opening_hours(
    hours: hours_schemas.OpeningHoursCreate, db: Session = Depends(get_db)
):
    return hours_db.create_opening_hours(db=db, hours=hours)


@router.get("/{hours_id}", response_model=hours_schemas.OpeningHours)
def read_opening_hours_by_id(hours_id: int, db: Session = Depends(get_db)):
    db_hours = hours_db.get_opening_hours_by_id(db, hours_id=hours_id)
    if db_hours is None:
        raise HTTPException(status_code=404, detail="Opening hours not found")
    return db_hours


@router.get("/location/{location_id}", response_model=List[hours_schemas.OpeningHours])
def read_opening_hours_by_location(location_id: int, db: Session = Depends(get_db)):
    return hours_db.get_opening_hours_by_location(db, location_id=location_id)


@router.put("/{hours_id}", response_model=hours_schemas.OpeningHours)
def update_opening_hours(
    hours_id: int,
    hours: hours_schemas.OpeningHoursUpdate,
    db: Session = Depends(get_db),
):
    db_hours = hours_db.update_opening_hours(db, hours_id=hours_id, hours=hours)
    if db_hours is None:
        raise HTTPException(status_code=404, detail="Opening hours not found")
    return db_hours


@router.delete("/{hours_id}")
def delete_opening_hours(hours_id: int, db: Session = Depends(get_db)):
    db_hours = hours_db.delete_opening_hours(db, hours_id=hours_id)
    if db_hours is None:
        raise HTTPException(status_code=404, detail="Opening hours not found")
    return {"message": "Opening hours deleted successfully"}
