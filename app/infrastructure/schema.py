from infrastructure.db import Base
from sqlalchemy import Column, Integer, String, Text
from infrastructure.db import SessionLocal

# from .db import BaseMixin


class WorkOrderRecord(Base):
    __tablename__ = "work_orders"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    process_routing_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<WorkOrder id={self.id}>"

    def process_routing(self) -> "ProcessRoutingRecord":
        db = SessionLocal()
        return db.query(ProcessRoutingRecord).filter_by(
            id=self.process_routing_id
        ).first()

    def process_routing_description(self) -> str:
        return self.process_routing().description

    def item(self) -> "ItemRecord":
        db = SessionLocal()
        return db.query(ItemRecord).filter_by(id=self.process_routing().item_id).first()

    def item_number(self) -> str:
        return self.item().item_number

    def item_description(self) -> str:
        return self.item().description


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
