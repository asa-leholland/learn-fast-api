from models.Item import Item, ItemCategory

items = {
    0: Item(name="Test", price=9.99, count=20, id=0, category=ItemCategory.TEST),
    1: Item(name="Pliers", price=5.99, count=20, id=1, category=ItemCategory.TOOLS),
    2: Item(name="Nails", price=1.99, count=100, id=2, category=ItemCategory.CONSUMABLES),
}
