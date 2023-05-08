from typing import List

from application.Item import ItemApp
from fastapi import APIRouter, HTTPException, status
from infrastructure.database import SessionLocal
from infrastructure.schema import ItemRecord
from pydantic import BaseModel
from presentation.items import ItemDTO


class ModuleDTO(BaseModel):
    id: int
    item: ItemDTO
    serial_number: str or None

    class Config:
        orm_mode = True
