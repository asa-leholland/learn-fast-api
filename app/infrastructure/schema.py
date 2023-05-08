from sqlalchemy import Column, Integer, String

from .db import BaseMixin




class WorkOrderRecord(BaseMixin):
    __tablename__ = "work_orders"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)


class ModuleRecord(BaseMixin):
    __tablename__ = "modules"

    id = Column(Integer, primary_key=True, index=True)
    serial_number = Column(String)
    work_order_id = Column(Integer)


class ItemRecord(BaseMixin):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    item_number = Column(String)
    description = Column(String)


class ProcessRoutingRecord(BaseMixin):
    __tablename__ = "process_routing"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer)
    description = Column(String)
