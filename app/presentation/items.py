from typing import List

from application.Item import ItemApp
from fastapi import APIRouter, HTTPException, status
from infrastructure.database import SessionLocal
from infrastructure.schema import ItemRecord
from pydantic import BaseModel

router = APIRouter()

db = SessionLocal()


class NewItemDTO(BaseModel):
    item_number: str
    description: str

    class Config:
        orm_mode = True


class ItemDTO(BaseModel):
    id: int
    item_number: str
    description: str

    class Config:
        orm_mode = True


@router.get('/items', response_model=List[ItemDTO], status_code=200)
def get_all_items():
    return db.query(ItemRecord).all()


@router.get('/item/id/{item_id}', response_model=ItemDTO, status_code=status.HTTP_200_OK)
def get_an_item_by_item_id(item_id: int):
    if (
        item := db.query(ItemRecord)
        .filter(ItemRecord.id == item_id)
        .first()
    ):
        return item
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


@router.get('/item/part_number/{item_part_no}', response_model=ItemDTO or None, status_code=status.HTTP_200_OK)
def get_an_item_by_part_number(item_part_no: str):
    if (
        item := db.query(ItemRecord)
        .filter(ItemRecord.item_number == item_part_no)
        .first()
    ):
        return item
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


@router.post('/items', response_model=NewItemDTO, status_code=status.HTTP_201_CREATED)
def create_an_item(item: NewItemDTO):
    if int(item.item_number) < 1:
        raise HTTPException(status_code=400, detail="Item Number must be a positive numeric string.")
    if not item.description:
        raise HTTPException(status_code=400, detail="Item description must be provided.")

    db_item = db.query(ItemRecord).filter(ItemRecord.item_number == item.item_number).first()

    if db_item is not None:
        raise HTTPException(status_code=400, detail="Item number already exists")

    new_item = ItemRecord(
        item_number=item.item_number,
        description=item.description,
    )

    db.add(new_item)
    db.commit()

    return new_item

# Commented out for reference, but not used in this example
# @router.put('/item/{item_id}', response_model=ItemDTO, status_code=status.HTTP_200_OK)
# def update_an_item(item_id: int, item: ItemDTO):
#     item_to_update = db.query(schema.ItemRecord).filter(schema.ItemRecord.id == item_id).first()
#     item_to_update.item_number = item.item_number
#     item_to_update.description = item.description

#     db.commit()

#     return item_to_update


# @app.delete('/item/{item_id}')
# def delete_item(item_id: int):
#     item_to_delete = db.query(schema.ItemRecord).filter(schema.ItemRecord.id == item_id).first()

#     if item_to_delete is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")

#     db.delete(item_to_delete)
#     db.commit()

#     return item_to_delete




