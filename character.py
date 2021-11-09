class Character():
    """ This superclass is to create new characters in the game """

    # Create a new character instance
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.dialogue = None

    def __repr__(self):
        return f"{self.name}"

    # Describe the character
    def describe(self):
        print(f'{self.name} is here')
        print(self.description)

    # Talk to the character
    def talk(self):
        if self.dialogue is not None:
            print(f'{self.name} says: {self.dialogue}')
        else:
            print(self.name + " hasn't got anything to say.")
