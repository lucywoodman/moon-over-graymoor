# Import textwrap library to wrap strings to a set width
import textwrap as tr

# Creates an instance of the Area class 
class Area():

    def __init__(self, area_name):
        self.name = area_name
        self.description = None

    def set_description(self, area_description):
        self.description = tr.fill(area_description, width=80)

    def get_description(self):
        return self.description

    def set_name(self, area_name):
        self.name = area_name

    def get_name(self):
        return self.name

    def get_details(self):
        print(self.name)
        print("--------------------")
        print(f"{self.description}\n")
