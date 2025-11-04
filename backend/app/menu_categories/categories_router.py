from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.menu_categories import categories_schemas, categories_db

router = APIRouter()


@router.get("/", response_model=List[categories_schemas.Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = categories_db.get_categories(db, skip=skip, limit=limit)
    return categories


@router.post("/", response_model=categories_schemas.Category)
def create_category(
    category: categories_schemas.CategoryCreate, db: Session = Depends(get_db)
):
    db_category = categories_db.get_category_by_name(db, name=category.name)
    if db_category:
        raise HTTPException(status_code=400, detail="Category already exists")
    return categories_db.create_category(db=db, category=category)


@router.get("/{category_id}", response_model=categories_schemas.Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = categories_db.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@router.put("/{category_id}", response_model=categories_schemas.Category)
def update_category(
    category_id: int,
    category: categories_schemas.CategoryUpdate,
    db: Session = Depends(get_db),
):
    db_category = categories_db.update_category(
        db, category_id=category_id, category=category
    )
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = categories_db.delete_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted successfully"}
