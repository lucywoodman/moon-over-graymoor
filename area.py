import textwrap as tr

class Area():
    """ This class is to create new areas in the game """

    # Create a new area instance
    def __init__(self, area_name):
        self.name = area_name
        self.description = None
        self.linked_areas = {}

    # Set the description of the area
    def set_description(self, area_description):
        self.description = tr.fill(area_description, width=80)

    # Get the description of the area
    def get_description(self):
        return self.description

    # Set the name of the area
    def set_name(self, area_name):
        self.name = area_name

    # Get the name of the area
    def get_name(self):
        return self.name

    # Connect to other areas
    def link_area(self, area_to_link, direction):
        self.linked_areas[direction] = area_to_link

    # Describe the area in the game
    def describe(self):
        print(f"{self.name}")
        print("-" * 80)
        print(f"{self.description}\n")
        print("**List of area items or points of interest will go here**\n")
        for direction in self.linked_areas:
            area = self.linked_areas[direction]
            print(f"- {area.get_name()} is to the [{direction}]")
        print("-" * 80)

    def move(self, direction):
        if direction in self.linked_areas:
            return self.linked_areas[direction]
        else:
            print("You can't go that way")
            return self