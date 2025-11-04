from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.menu_items import items_schemas, items_db

router = APIRouter()


@router.get("/", response_model=List[items_schemas.MenuItem])
def read_menu_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = items_db.get_menu_items(db, skip=skip, limit=limit)
    return items


@router.post("/", response_model=items_schemas.MenuItem)
def create_menu_item(item: items_schemas.MenuItemCreate, db: Session = Depends(get_db)):
    return items_db.create_menu_item(db=db, item=item)


@router.get("/{item_id}", response_model=items_schemas.MenuItem)
def read_menu_item(item_id: int, db: Session = Depends(get_db)):
    db_item = items_db.get_menu_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return db_item


@router.put("/{item_id}", response_model=items_schemas.MenuItem)
def update_menu_item(
    item_id: int, item: items_schemas.MenuItemUpdate, db: Session = Depends(get_db)
):
    db_item = items_db.update_menu_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return db_item


@router.delete("/{item_id}")
def delete_menu_item(item_id: int, db: Session = Depends(get_db)):
    db_item = items_db.delete_menu_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return {"message": "Menu item deleted successfully"}
