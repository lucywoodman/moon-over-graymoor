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
        print(self.characters)

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
        item_dict = {k: v for k, v in enumerate(self.items)}
        for key in item_dict.keys():
            print(key, '--', item_dict[key] )

    def list_chars(self):
        char_dict = {k: v for k, v in enumerate(self.characters)}
        for key in char_dict.keys():
            print(key, '--', char_dict[key] )

    def move(self, direction):
        if direction in self.linked_areas:
            return self.linked_areas[direction]
        else:
            print("You can't go that way")
            return self

    def check_for_chars(self):
        if self.characters:
            print('- There are people to [talk] to nearby')
        else:
            print('- (There is nobody nearby)')

    def check_for_items(self):
        if self.items:
            print('- There are items to [take] nearby')
        else:
            print('- (There are no items nearby)')
