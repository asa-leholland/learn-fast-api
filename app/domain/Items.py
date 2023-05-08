# from enum import Enum
# from pydantic import BaseModel, Field
# from typing import List

# class Item(BaseModel):
#     id: int = Field(ge=0)
#     name: str
#     price: float
#     count: int
#     category: ItemCategory

# class ItemCategory(str, Enum):
#     FOOD = "food"
#     CLOTHING = "clothing"
#     ELECTRONICS = "electronics"
#     HOME = "home"

# class ItemRepository:
#     def __init__(self):
#         self.items = {}

#     def get_all_items(self):
#         return list(self.items.values())

#     def add_item(self, item: Item):
#         if item.id in self.items:
#             raise ValueError(f"Item with {item.id=} already exists.")
#         self.items[item.id] = item

#     def get_item_by_id(self, item_id: int) -> Item:
#         if item_id not in self.items:
#             raise ValueError(f"Item with {item_id=} does not exist.")
#         return self.items[item_id]

#     def update_item(self, item_id: int, name: str | None = None, price: float | None = None, count: int | None = None):
#         if item_id not in self.items:
#             raise ValueError(f"Item with {item_id=} does not exist.")
#         item = self.items[item_id]
#         if name is not None:
#             item.name = name
#         if price is not None:
#             item.price = price
#         if count is not None:
#             item.count = count
#         self.items[item_id] = item
