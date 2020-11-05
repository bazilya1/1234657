class Balance:
    def __init__(self):
        self.l = 0
        self.r = 0

    def add_right(self, q):
        self.r += q

    def add_left(self, q):
        self.l += q

    def result(self):
        if self.r == self.l:
            print("=")
        elif self.r < self.l:
            print('L')
        elif self.r > self.l:
            print('R')
