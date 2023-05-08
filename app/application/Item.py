from typing import List

from infrastructure.db import SessionLocal
from infrastructure.schema import ItemRecord
from domain.Item import Item


class ItemApp:
    def __init__(self, item_record_table: ItemRecord):
        self._item_record_table = item_record_table

    # add method to get available routings, their IDs and their descriptions
    def get_available_items(self) -> List[ItemRecord]:
        db = SessionLocal()
        return db.query(self._item_record_table).all()

    def add_item(self, number: str, description: str) -> Item:
        db = SessionLocal()
        if db.query(self._item_record_table).filter(item_number=number).first():
            raise ValueError("Item number already exists.")

        # create domain Item
        new_item = Item(number=number, description=description)

        # record ItemRecord to db
        new_item_record = ItemRecord(item_number=number, description=description)
        db.add(new_item_record)
        db.commit()

        return new_item
