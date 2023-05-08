
from fastapi import FastAPI, HTTPException, status
from presentation import work_orders, items

from typing import Optional, List
from infrastructure.database import SessionLocal
from infrastructure import schema

# You can give your API a title and add additional metadata such as a description, version number, etc.
# The description also supports markdown formatting.
app = FastAPI(
    title="Work Order API",
    description="Lets you create and add traceability records to work orders.",
    version="0.1.0",
)


# app.include_router(work_orders.router)
app.include_router(items.router)
