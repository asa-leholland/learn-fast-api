from fastapi import APIRouter, HTTPException
from application.WorkOrder import WorkOrderApp
from application.ProcessRouting import ProcessRoutingApp
from infrastructure.schema import WorkOrderRecord, ItemRecord, ProcessRoutingRecord
from typing import List


router = APIRouter()


@router.post("/work_orders/", response_model=List[str])
async def create_work_order(quantity: int, item_id: int):
    if quantity < 1:
        raise HTTPException(status_code=400, detail="Quantity must be greater than 0.")
    if not item_id:
        raise HTTPException(status_code=400, detail="Item id must be provided.")
    service = WorkOrderApp(
        work_order_record=WorkOrderRecord,
        )
    new_work_order = service.create_work_order(quantity)
    return new_work_order.serial_numbers


# define an endpoint that returns a list of available routings for new work orders
@router.get("/work_orders/routings/", response_model=List[str])
async def get_available_routings():
    service = ProcessRoutingApp(ProcessRoutingRecord)
    return service.get_available_routings()
