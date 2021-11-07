from gameinfo import GameInfo
from chapter import Chapter
from area import Area
from character import Character

# Create the game title
mog_game = GameInfo("Moon Over Graymoor")
mog_game.welcome()

# Create the chapter title
chap_one = Chapter("one")
chap_one.title()

# Create the areas
town_square = Area("Town Square")
town_square.set_description("A light mist drifts from the loamy sky above you. The drizzle quickly freezes into glass in the streets. In the middle of the small town’s square, Graymoor’s blacksmith, George Gilly, lies face down in the snow, still, and ashen.")
town_square.describe()

oswald = Character("Oswald the Coroner", "An impatient, very finely dressed man.")
oswald.describe()