class Item():

    # Create a new item instance
    def __init__(self, item_name, item_description):
        self.name = item_name
        self.description = item_description

    def __repr__(self):
        return f"{self.name}"

    # Describe the item
    def describe(self):
        print(f"{self.name} is here")
        print(self.description)