from typing import List

from domain.WorkOrder import WorkOrder
from domain.ProcessRouting import ProcessRouting
from domain.Item import Item
from infrastructure.db import SessionLocal
from infrastructure.schema import WorkOrderRecord, ModuleRecord, ItemRecord, ProcessRoutingRecord


class WorkOrderApp:
    def __init__(
            self,
            work_order_table=WorkOrderRecord,
            process_routing_table=ProcessRoutingRecord,
            module_table=ModuleRecord):
        self.work_order_table = work_order_table
        self.process_routing_table = process_routing_table
        self.module_table = module_table

    def create_work_order(self, module_quantity: int, process_routing_id: int) -> WorkOrderRecord:
        if module_quantity < 1:
            raise ValueError("Quantity must be greater than 0.")

        with SessionLocal() as db:
            # read process routing from db
            process_routing_record = db.query(self.process_routing_table).filter(self.process_routing_table.id == process_routing_id).first()
            if not process_routing_record:
                raise ValueError(f"Process Routing with id {process_routing_id} not found.")

            # form a domain Item object from the process routing record
            item_record = db.query(ItemRecord).filter(ItemRecord.id == process_routing_record.item_id).first()
            module_item = Item(
                number=item_record.item_number,
                description=item_record.description
            )

            # run domain logic
            work_order = WorkOrder(quantity=module_quantity, module_item=module_item)

            # write work order to db
            new_work_order_record = WorkOrderRecord(quantity=10, process_routing_id=process_routing_id)
            db.add(new_work_order_record)

            # write modules to db
            for module in work_order.modules:
                new_module = ModuleRecord(serial_number=module.serial_number, work_order_id=new_work_order_record.id)
                db.add(new_module)

            db.commit()

            db.refresh(new_work_order_record)

        return new_work_order_record
