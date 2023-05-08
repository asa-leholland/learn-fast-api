from sqlalchemy.orm import joinedload
from infrastructure.schema import WorkOrderRecord, ProcessRoutingRecord, ItemRecord, ModuleRecord
from infrastructure.db import SessionLocal



def get_all_work_orders():
    with SessionLocal() as db:
        return (
            db.query(WorkOrderRecord)
            .join(ProcessRoutingRecord, WorkOrderRecord.process_routing_id == ProcessRoutingRecord.id)
            .join(ItemRecord, ProcessRoutingRecord.item_id == ItemRecord.id)
            .options(joinedload('process_routing').joinedload('item'))
            .all()
        )
