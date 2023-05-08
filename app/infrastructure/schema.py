from infrastructure.db import Base
from sqlalchemy import Column, Integer, String, Text

# from .db import BaseMixin


class WorkOrderRecord(Base):
    __tablename__ = "work_orders"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    process_routing_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<WorkOrder id={self.id}>"


class ModuleRecord(Base):
    __tablename__ = "modules"

    id = Column(Integer, primary_key=True, index=True)
    serial_number = Column(String)
    work_order_id = Column(Integer)

    def __repr__(self):
        return f"<Module serial_number={self.serial_number}>"


class ItemRecord(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    item_number = Column(String(255), nullable=False, unique=True)
    description = Column(Text)

    def __repr__(self):
        return f"<Item item_number={self.item_number}>"


class ProcessRoutingRecord(Base):
    __tablename__ = "process_routings"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer)
    description = Column(String)

    def __repr__(self):
        return f"<ProcessRouting item_id={self.item_id}>"
