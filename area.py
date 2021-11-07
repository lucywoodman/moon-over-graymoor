import textwrap as tr

class Area():
    """ This class is to create new areas in the game """

    # Create a new area instance
    def __init__(self, area_name):
        self.name = area_name
        self.description = None
        self.linked_areas = {}
        self.characters = []
        self.items = []

    # Set/Get the description of the area
    def set_description(self, area_description):
        self.description = tr.fill(area_description, width=80)

    def get_description(self):
        return self.description

    # Set/Get the name of the area
    def set_name(self, area_name):
        self.name = area_name

    def get_name(self):
        return self.name

    # Set characters to the area
    def set_character(self, character_name):
        self.characters.append(character_name)

    # Set items in the area
    def set_item(self, item_name):
        self.items.append(item_name)

    # Connect to other areas
    def link_area(self, area_to_link, direction):
        self.linked_areas[direction] = area_to_link

    # Describe the area in the game
    def describe(self):
        print(f"{self.name}")
        print("-" * 80)
        print(f"{self.description}\n")
        for direction in self.linked_areas:
            area = self.linked_areas[direction]
            print(f"- {area.get_name()} is to the [{direction}]")

    def list_items(self):
        print("\nItems nearby:")
        for item in self.items:
            print(f"- {item}")

    def list_chars(self):
        print("\nPeople nearby:")
        for char in self.characters:
            print(f"- {char}")

    def move(self, direction):
        if direction in self.linked_areas:
            return self.linked_areas[direction]
        else:
            print("You can't go that way")
            return self