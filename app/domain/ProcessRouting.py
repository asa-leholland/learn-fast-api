import uuid

from .Item import Item


class ProcessRouting:
    def __init__(self, item: Item):
        self.id = str(uuid.uuid4())
        self.item = item
