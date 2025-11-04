from sqlalchemy.orm import Session
from app.menu_items.items_models import MenuItem
from app.menu_items import items_schemas


def get_menu_item(db: Session, item_id: int):
    return db.query(MenuItem).filter(MenuItem.id == item_id).first()


def get_menu_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(MenuItem).offset(skip).limit(limit).all()


def get_menu_items_by_category(db: Session, category_id: int):
    return db.query(MenuItem).filter(MenuItem.category_id == category_id).all()


def create_menu_item(db: Session, item: items_schemas.MenuItemCreate):
    db_item = MenuItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_menu_item(db: Session, item_id: int, item: items_schemas.MenuItemUpdate):
    db_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if db_item:
        update_data = item.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item


def delete_menu_item(db: Session, item_id: int):
    db_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
