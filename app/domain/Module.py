import uuid


class Module:
    def __init__(self, item_number: str, revision: str, item_description: str):
        self.id = str(uuid.uuid4())
        self.item_number = item_number
        self.revision = revision
        self.part_number = f'{self.item_number}:{self.revision}'
        self.serial_number = None

    def __str__(self):
        return f'{self.part_number} ({self.description})'

    def __repr__(self):
        return self.__str__()

    def assign_serial_number(self, serial_number: str):
        self.serial_number = serial_number
