
from fastapi import FastAPI
from presentation import work_orders, items, process_routings

app = FastAPI(
    title="Work Order API",
    description="The Work Order API lets you <i><b>create new work orders</b></i> and <i><b>add traceability records</b></i> to existing work orders.",
    version="0.1.0",
)

app.include_router(work_orders.router)
app.include_router(items.router)
app.include_router(process_routings.router)
