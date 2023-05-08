from typing import List

from application.Item import ItemApp
from fastapi import APIRouter, HTTPException, status
from infrastructure.database import SessionLocal
from infrastructure.schema import ProcessRoutingRecord, ItemRecord
from pydantic import BaseModel
from presentation.items import ItemDTO

router = APIRouter()

db = SessionLocal()


class ProcessRoutingDTO(BaseModel):
    id: int
    description: str
    item: ItemDTO

    class Config:
        orm_mode = True


@router.get('/process_routings', response_model=List[ProcessRoutingDTO], status_code=200)
def get_all_process_routings():

    process_routing_dtos = []
    for process_routing in db.query(ProcessRoutingRecord).all():
        item_record = db.query(ItemRecord).filter(ItemRecord.id == process_routing.item_id).first()
        item_dto = ItemDTO(
            id=item_record.id,
            item_number=item_record.item_number,
            description=item_record.description
            )
        process_routing_dtos.append(
            ProcessRoutingDTO(
                id=process_routing.id,
                description=process_routing.description,
                item=item_dto
                ))

    return process_routing_dtos
