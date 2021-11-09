class Chapter():

    def __init__(self, chapter):
        self.chapter = chapter

    def title(self):
        title = f"DAY {self.chapter.upper()}"
        print("\n")
        print("=" * len(title))
        print(title)
        print("=" * len(title))