from gameinfo import GameInfo
from chapter import Chapter
from area import Area
from character import Character
from item import Item

# Create the game title
mog_game = GameInfo('Moon Over Graymoor')
mog_game.welcome()
mog_game.backstory()

# Create the chapter titles
chap_one = Chapter('one')

# Create the areas
town_square = Area('The Town Square')
town_square.set_description('A light mist drifts from the loamy sky above you. The drizzle quickly freezes into glass in the streets. In the middle of the small town’s square, Graymoor’s blacksmith, George Gilly, lies face down in the snow, still, and ashen.')

gillys_house = Area('George Gilly\'s House')
gillys_house.set_description('The doors and windows hang open, and the curtains shiver in the frigid wind. Snow has begun to creep onto the sills, and over the threshold, into the dark and empty home. As you enter, you find the floorboards in the kitchen have been pried up, and on the table next to them sits a small, artless lockbox.')

# Link areas
town_square.link_area(gillys_house, 'north')
gillys_house.link_area(town_square, 'south')

# Create the characters
oswald = Character('Oswald the Coroner', 'An impatient, very finely dressed man')
sagh = Character('Sagh Gazara', 'The proprietor of the Graymoor Bend inn')

# Link characters to areas
town_square.set_character(oswald)
town_square.set_character(sagh)

# Create items
lockbox = Item('Lockbox', 'Small, artless lockbox')

# Link items to areas
gillys_house.set_item(lockbox)

# Set game defaults
current_area = town_square
current_area_seen = False
alive = True

def first_chapter():
    while alive is True:
        global current_area
        global current_area_seen
        print('\n')
        
        # If the current area's description hasn't been seen yet, display it.
        if current_area_seen == False:
            current_area.describe()
            current_area_seen = True

        # If there are items or characters nearby, list them.
        if current_area.items:
            current_area.list_items()

        if current_area.characters:
            current_area.list_chars()
        
        print('-' * 80)
        command = input('What would you like to do?\n> ')

        # If the command is one of the directions, update the current area.
        if command in ['north', 'south', 'east', 'west']:
            current_area = current_area.move(command)
            current_area_seen = False
        else:
            print('Please type a command')

def second_chapter():
    print('Second chapter will go here')

menu_options = {
    1: 'Chapter One',
    2: 'Chapter Two',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
            current_chapter = chap_one
            current_chapter.title()
            first_chapter()
        elif option == 2:
            second_chapter()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
