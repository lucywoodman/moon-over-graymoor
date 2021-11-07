import textwrap as tr

class Area():
    """ This class is to create new areas in the game """

    # Create a new area instance
    def __init__(self, area_name):
        self.name = area_name
        self.description = None

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

    # Describe the area in the game
    def describe(self):
        print(self.name)
        print("--------------------")
        print(f"{self.description}\n")
