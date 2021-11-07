class GameInfo():

    def __init__(self, game_title):
        self.title = game_title

    def welcome(self):
        print("-----------------------------")
        print(f"Welcome to {self.title}")
        print("-----------------------------")

    def backstory(self):
        print("**Scene setting will go here**\n")
