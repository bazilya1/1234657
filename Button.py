class Button:
    def __init__(self):
        self.a = 0

    def click(self):
        self.a += 1
        print(self.a)

    def click_count(self):
        self.a -= 1
        print(self.a)

    def reset(self):
        self.a = 0
        print(self.a)
