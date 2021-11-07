from area import Area
from character import Character
from gameinfo import GameInfo

mog_game = GameInfo("Moon Over Graymoor")
mog_game.welcome()

town_square = Area("Town Square")
town_square.set_description("A light mist drifts from the loamy sky above you. The drizzle quickly freezes into glass in the streets. In the middle of the small town’s square, Graymoor’s blacksmith, George Gilly, lies face down in the snow, still, and ashen.")
town_square.describe()

oswald = Character("Oswald the Coroner", "A bossy, impatient, and very finely dressed man.")
oswald.describe()