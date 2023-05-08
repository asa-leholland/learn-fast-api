from typing import List

from domain.WorkOrder import WorkOrder
from infrastructure.db import SessionLocal
from infrastructure.schema import WorkOrderRecord, ModuleRecord, ItemRecord, ProcessRoutingRecord


class WorkOrderApp:
    def __init__(
            self,
            work_order_record=WorkOrderRecord,
            process_routing_record=ProcessRoutingRecord,
            module_record=ModuleRecord):
        self.work_order_record = work_order_record
        self.process_routing_record = process_routing_record
        self.module_record = module_record

    def create_work_order(self, module_quantity: int, process_routing_id: int) -> WorkOrder:
        if module_quantity < 1:
            raise ValueError("Quantity must be greater than 0.")

        # read process routing from db
        db = SessionLocal()
        process_routing = db.query(self.process_routing_record).filter(self.process_routing_record.id == process_routing_id).first()
        if not process_routing:
            raise ValueError(f"Process Routing with id {process_routing_id} not found.")

        # run domain logic
        work_order = WorkOrder(quantity=module_quantity, item=process_routing.item)

        # write work order to db
        new_work_order_record = WorkOrderRecord(quantity=10, process_routing_id=process_routing_id)
        db.add(new_work_order_record)
        db.commit()

        # write modules to db
        for module in work_order.modules:
            new_module = ModuleRecord(serial_number=module, work_order_id=new_work_order_record.id)
            db.add(new_module)
        db.commit()

        return new_work_order_record
