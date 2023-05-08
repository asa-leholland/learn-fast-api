from fastapi import APIRouter, HTTPException, Depends
from application.Item import ItemApp
from infrastructure.schema import ItemRecord
from typing import List
from infrastructure.db import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/items/", response_model=List[str])
async def create_item(item_number: int, item_description: str):
    if item_number < 1:
        raise HTTPException(status_code=400, detail="Item Number must be a positive integer.")
    if not item_description:
        raise HTTPException(status_code=400, detail="Item description must be provided.")
    # check if item number already exists
    service = ItemApp(ItemRecord)
    if service.get_item_by_number(item_number):
        raise HTTPException(status_code=400, detail="Item number already exists.")

    return service.create_item(item_number, item_description)


@router.get("/items/", response_model=List[str])
async def get_available_items(db: Session = Depends(get_db)):
    items = db.query(ItemRecord).all()
    return {"items": items}
