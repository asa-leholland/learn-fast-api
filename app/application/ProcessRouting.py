from typing import List

from domain.ProcessRouting import ProcessRouting
from infrastructure.db import SessionLocal
from infrastructure.schema import ItemRecord, ProcessRoutingRecord
from dataclasses import dataclass


class ProcessRoutingApp:
    def __init__(self, item_record: ItemRecord, process_routing_record: ProcessRoutingRecord):
        self._item_record = item_record
        self._process_routing_record = process_routing_record

    # add method to get available routings, their IDs and their descriptions
    def get_available_routings(self) -> List[ProcessRouting]:
        db = SessionLocal()
        return db.query(self._process_routing_record).all()

    def add_process_routing(self, description: str, item_id: int) -> ProcessRouting:
        db = SessionLocal()
        item = db.query(self._item_record).filter(self._item_record.id == item_id).first()
        if not item:
            raise ValueError("Item not found.")
        new_routing = ProcessRoutingRecord(description=description, item_id=item_id)
        db.add(new_routing)
        db.commit()
        return new_routing
