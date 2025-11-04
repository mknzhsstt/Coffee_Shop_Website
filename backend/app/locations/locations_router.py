from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.locations import locations_schemas, locations_db

router = APIRouter()


@router.get("/", response_model=List[locations_schemas.Location])
def read_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    locations = locations_db.get_locations(db, skip=skip, limit=limit)
    return locations


@router.post("/", response_model=locations_schemas.Location)
def create_location(
    location: locations_schemas.LocationCreate, db: Session = Depends(get_db)
):
    return locations_db.create_location(db=db, location=location)


@router.get("/{location_id}", response_model=locations_schemas.Location)
def read_location(location_id: int, db: Session = Depends(get_db)):
    db_location = locations_db.get_location(db, location_id=location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location


@router.put("/{location_id}", response_model=locations_schemas.Location)
def update_location(
    location_id: int,
    location: locations_schemas.LocationUpdate,
    db: Session = Depends(get_db),
):
    db_location = locations_db.update_location(
        db, location_id=location_id, location=location
    )
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location


@router.delete("/{location_id}")
def delete_location(location_id: int, db: Session = Depends(get_db)):
    db_location = locations_db.delete_location(db, location_id=location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return {"message": "Location deleted successfully"}
