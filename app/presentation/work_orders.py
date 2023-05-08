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

from presentation.process_routings import ProcessRoutingDTO
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


# # define an endpoint that returns a list of available routings for new work orders
# @router.get("/work_orders/", response_model=List[str])
# async def get_available_routings():
#     # service = ProcessRoutingApp(ProcessRoutingRecord)
#     # return service.get_available_routings()


#     module_dtos = [
#         ModuleDTO(serial_number=module) for module in work_order.modules
#     ]

#         WorkOrderDTO(
#             id=new_work_order.id,
#             process_routing=process_routing,
#             modules=module_dtos,
#         )

#     return new_work_order
