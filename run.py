from gameinfo import GameInfo
from chapter import Chapter
from area import Area
from character import Character

# Create the game title
mog_game = GameInfo("Moon Over Graymoor")
mog_game.welcome()
mog_game.backstory()

# Create the chapter title
chap_one = Chapter("one")
chap_one.title()

# Create the areas
town_square = Area("The Town Square")
town_square.set_description("A light mist drifts from the loamy sky above you. The drizzle quickly freezes into glass in the streets. In the middle of the small town’s square, Graymoor’s blacksmith, George Gilly, lies face down in the snow, still, and ashen.")

gillys_house = Area("George Gilly's House")
gillys_house.set_description("The doors and windows hang open, and the curtains shiver in the frigid wind. Snow has begun to creep onto the sills, and over the threshold, into the dark and empty home. As you enter, you find the floorboards in the kitchen have been pried up, and on the table next to them sits a small, artless lockbox.")

town_square.link_area(gillys_house, "north")
gillys_house.link_area(town_square, "south")

current_area = town_square
alive = True

while alive == True:
    print("\n")
    current_area.describe()
    
    command = input("What would you like to do?\n> ")

    if command in ["north", "south", "east", "west"]:
        current_area = current_area.move(command)
    else:
        print("Please type a direction")