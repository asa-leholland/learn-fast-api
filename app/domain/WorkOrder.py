import uuid

from .Module import Module
from .Item import Item


class WorkOrder:
    def __init__(self, quantity: int, module_item: Item):
        self.id = str(uuid.uuid4())
        self.quantity = quantity
        self.item = module_item
        self.serial_numbers = self.generate_serial_numbers()
        self.modules = self.generate_modules()

    def generate_serial_numbers(self):
        return [str(uuid.uuid4()) for _ in range(self.quantity)]

    def generate_modules(self):
        return [
            Module(serial_number=serial_number)
            for serial_number in self.serial_numbers
        ]
