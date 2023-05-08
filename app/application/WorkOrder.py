from typing import List

from domain.WorkOrder import WorkOrder
from infrastructure.db import SessionLocal
from infrastructure.schema import WorkOrderRecord, ModuleRecord, ItemRecord
from dataclasses import dataclass

@dataclass
class WorkOrderPersistence:
    work_order_record: WorkOrderRecord
    module_record: ModuleRecord
    item_record: ItemRecord




class WorkOrderApp:
    def __init__(self, persistence: WorkOrderPersistence):
        self._persistence = persistence


    def create_work_order(self, quantity: int, item_id: int) -> List[str]:
        if quantity < 1:
            raise ValueError("Quantity must be greater than 0.")

        # read item from db
        db = SessionLocal()
        item = db.query(self._persistence.item_record).filter(self._persistence.item_record.id == item_id).first()
        if not item:
            raise ValueError("Item not found.")

        # run domain logic
        work_order = WorkOrder(quantity=quantity, item=item)

        work_order.assign_routing(item.process_routing)

        # write work order to db
        new_work_order = WorkOrderRecord(quantity=10)
        db.add(new_work_order)
        db.commit()

        # write modules to db
        for module in work_order.modules:
            new_module = ModuleRecord(serial_number=module, work_order_id=new_work_order.id)
            db.add(new_module)
        db.commit()

        return work_order.serial_numbers
