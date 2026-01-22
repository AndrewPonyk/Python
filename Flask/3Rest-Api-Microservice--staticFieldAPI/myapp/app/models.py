# Models for the application
# Add your data models here

_items_store = {}
_next_id = 1

class Item:
    def __init__(self, id, name, description=None):
        self.id = id
        self.name = name
        self.description = description

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

    def update_description(self, new_description):
        """Updates the description of this specific item."""
        self.description = new_description

    @staticmethod
    def add_item(name, description=None):
        global _next_id # Use global to modify the module-level variable
        item_id = _next_id
        _next_id += 1
        item = Item(item_id, name, description)
        _items_store[item_id] = item
        return item

    @staticmethod
    def get_item_by_id(item_id):
        return _items_store.get(item_id)

    @staticmethod
    def get_all_items():
        return list(_items_store.values())

