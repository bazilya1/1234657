class Button:
    global a
    a = 0
    def click(self):
        global a
        a += 1
        print(a)

    def click_count(self):
        global a
        a -= 1
        print(a)

    def reset(self):
        global a
        a = 0
        print(a)
