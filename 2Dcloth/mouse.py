

class Mouse:

    def __init__(self):
        self.pos = None
        self.previous_pos = None
        self.click_left = False
        self.click_right = False

    def set_pos(self,pos):
        if self.pos is not None:
            self.previous_pos = self.pos
            self.pos = pos
        else:
            self.previous_pos = pos
            self.pos = pos

    def set_click_left(self,value):
        self.click_left = value
        self.click_right = False

    def set_click_right(self, value):
        self.click_right = value
        self.click_left = False
