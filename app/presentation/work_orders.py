from fastapi import APIRouter, HTTPException
from application.WorkOrder import WorkOrderApp
from application.ProcessRouting import ProcessRoutingApp
from infrastructure.schema import WorkOrderRecord, ModuleRecord, ProcessRoutingRecord
from typing import List
from datetime import datetime

from application.Item import ItemApp
from fastapi import APIRouter, HTTPException, status
from infrastructure.database import SessionLocal
from pydantic import BaseModel

from presentation.modules import ModuleDTO
# from presentation.users import UserDTO
from presentation.items import ItemDTO

router = APIRouter()


class WorkOrderDTO(BaseModel):
    id: int

    class Config:
        orm_mode = True


@router.post("/work_orders/", response_model=WorkOrderDTO, status_code=status.HTTP_201_CREATED)
async def create_work_order(module_quantity: int, process_routing_id: int):
    if module_quantity < 1:
        raise HTTPException(status_code=400, detail="Module quantity must be greater than 0.")
    if not process_routing_id:
        raise HTTPException(status_code=400, detail="Process routing id must be provided.")

    service = WorkOrderApp(
        work_order_table=WorkOrderRecord,
        process_routing_table=ProcessRoutingRecord,
        module_table=ModuleRecord
        )

    try:
        new_work_order_record = service.create_work_order(module_quantity, process_routing_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

    return WorkOrderDTO(id=new_work_order_record.id)


class WorkOrderListEntryDTO(BaseModel):
    id: int
    process_routing_id: int
    process_routing_description: str
    item_number: str
    item_description: str
    module_quantity: int

    class Config:
        orm_mode = True


class ProcessRoutingDTO(BaseModel):
    id: int
    description: str
    item: ItemDTO

class WorkOrderDTO(BaseModel):
    id: int
    process_routing: ProcessRoutingDTO
    quantity: int

class AllWorkOrdersDTO(BaseModel):
    work_orders: List[WorkOrderDTO]

# define an endpoint that returns a list of available routings for new work orders
@router.get("/work_orders/", response_model=List[WorkOrderListEntryDTO])
async def get_all_work_orders():
    service = WorkOrderApp(WorkOrderRecord)
    work_order_records = service.get_work_orders()

    print(work_order_records)


    work_orders = []
    for work_order in work_order_records:
        work_orders.append(
            WorkOrderDTO(
                id=work_order.id,
                quantity=work_order.quantity,
                process_routing=ProcessRoutingDTO(
                    id=work_order.process_routing.id,
                    description=work_order.process_routing.description,
                    item=ItemDTO(
                        id=work_order.process_routing.item.id,
                        item_number=work_order.process_routing.item.item_number,
                        description=work_order.process_routing.item.description,
                    ),
                ),
            )
        )

    return AllWorkOrdersDTO(work_orders=work_orders)
