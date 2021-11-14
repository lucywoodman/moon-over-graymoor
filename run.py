import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('moon_over_graymoor')

login = SHEET.worksheet('login')
data = login.get_all_values()
print(data)

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

# Set the characters dialogue
oswald.set_dialogue('Testing, testing, 1, 2, 3...')
sagh.set_dialogue('Also, testing, testing, 1, 2, 3...')

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
            current_area.check_for_chars()
            current_area.check_for_items()
            current_area_seen = True
        
        print('-' * 80)
        command = input('What would you like to do: ')

        # If the command is one of the directions, update the current area.
        if command in ['north', 'south', 'east', 'west']:
            current_area = current_area.move(command)
            current_area_seen = False
        # If the command is "talk", offer the option of nearby characters.
        elif command == 'talk':
            talking = True
            while talking is True:
                character_list = current_area.list_chars()
                # Print the list of nearby characters
                print("\nPeople nearby:")
                for key in character_list:
                    print(key, '--', character_list[key] )
                print('9 -- Go back')
                # Ask which character would they like to talk to
                print('-' * 80)
                new_command = int(input('Who would you like to talk to: '))
                # Return selected character class
                if new_command in character_list:
                    char_to_talk = character_list.get(new_command)
                    print("\n")
                    char_to_talk.talk()
                elif new_command == 9:
                    talking = False
                    current_area_seen = False
                else:
                    print('Invalid option. Please enter an available number.')
        else:
            print('Please enter a valid command. E.g. talk')

def second_chapter():
    print('Second chapter will go here')

def third_chapter():
    print('Third chapter will go here')

# https://computinglearner.com/how-to-create-a-menu-for-a-python-console-application/
menu_options = {
    1: 'Chapter One',
    2: 'Chapter Two',
    3: 'Chapter Three',
    9: 'Exit'
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
            print('Wrong input. Please enter a number...')
        #Check what choice was entered and act accordingly
        if option == 1:
            current_chapter = chap_one
            current_chapter.title()
            first_chapter()
        elif option == 2:
            second_chapter()
        elif option == 3:
            third_chapter()
        elif option == 9:
            exit()
        else:
            print('Invalid option. Please enter an available number.')
# End code
