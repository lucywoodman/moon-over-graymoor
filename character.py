# import textwrap as tr

class Character():
    """ This superclass is to create new characters in the game """

    # Create a new character instance
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description

    # Describe the character
    def describe(self):
        print(f"{self.name} is here")
        print(self.description)
