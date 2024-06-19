

class Mouse:

    def __init__(self,pos):
        self.pos = pos
        self.previous_pos = pos
        self.click_left = False
        self.click_right = False

    def set_pos(self,pos):
        self.previous_pos = self.pos
        self.pos = pos

    def set_click_left(self,value):
        self.click_left = value
        self.click_right = False

    def set_click_right(self, value):
        self.click_right = value
        self.click_left = False
