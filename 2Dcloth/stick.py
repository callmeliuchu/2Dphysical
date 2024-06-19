from vec2 import Vec2


class Stick:

    def __init__(self,c1,c2):
        self.c1 = c1
        self.c2 = c2
        self.is_select = False
        self.is_active = True
        self.length = Vec2.length(self.c1.pos,self.c2.pos)

    def keep_length(self):
        if not self.is_active:
            return
        if not self.c1.is_pin and not self.c2.is_pin:
            current = Vec2.length(self.c1.pos,self.c2.pos)
            ratio = (current - self.length) / current * 0.5
            diff = self.c1.pos - self.c2.pos
            self.c1.pos -= diff * ratio
            self.c2.pos += diff * ratio
        if self.c1.is_pin and not self.c2.is_pin:
            current = Vec2.length(self.c1.pos,self.c2.pos)
            ratio = (current - self.length) / current
            diff = self.c1.pos - self.c2.pos
            self.c2.pos += diff * ratio
        if not self.c1.is_pin and self.c2.is_pin:
            current = Vec2.length(self.c1.pos,self.c2.pos)
            ratio = (current - self.length) / current
            diff = self.c1.pos - self.c2.pos
            self.c1.pos -= diff * ratio