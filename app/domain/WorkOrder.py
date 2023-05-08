import uuid

from .Module import Module
from .Item import Item


class WorkOrder:
    def __init__(self, quantity: int, item: Item):
        self.id = str(uuid.uuid4())
        self.quantity = quantity
        self.item = item
        self.serial_numbers = self.generate_serial_numbers()
        self.modules = self.generate_modules()

    def generate_serial_numbers(self):
        return [str(uuid.uuid4()) for _ in range(self.quantity)]

    def generate_modules(self):

        modules = []
        for serial_number in self.serial_numbers:
            module = Module(item_id=self.item.id, revision='A')
            module.assign_serial_number(serial_number)
            modules.append(module)
        return modules
