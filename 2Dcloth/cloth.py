from circle import Circle
from vec2 import Vec2


class Stick:

    def __init__(self,c1,c2):
        self.c1 = c1
        self.c2 = c2
        self.length = Vec2.length(self.c1.pos,self.c2.pos)

    def keep_length(self):
        current = Vec2.length(self.c1.pos,self.c2.pos)
        ratio = (current - self.length) / current * 0.5
        diff = self.c1.pos - self.c2.pos
        self.c1.pos -= diff * ratio
        self.c2.pos += diff * ratio


class Cloth:

    def __init__(self):
        c1 = Circle(Vec2(100, 100), 5, 10)
        c2 = Circle(Vec2(150, 100), 5, 10)
        c3 = Circle(Vec2(100, 150), 5, 10)
        c4 = Circle(Vec2(150, 150), 5, 10)
        self.circles = [c1,c2,c3,c4]
        s1 = Stick(c1,c2)
        s2 = Stick(c2,c3)
        s3 = Stick(c3,c4)
        s4 = Stick(c4,c1)
        s5 = Stick(c1,c3)
        s6 = Stick(c2,c4)
        self.sticks = [s1,s2,s3,s4,s5,s6]

    def add_force(self,force):
        for c in self.circles:
            c.add_force(force)

    def update(self,dt):
        for c in self.circles:
            c.update(dt)

        for stick in self.sticks:
            stick.keep_length()


    def keep_inside(self,w,h):
        for c in self.circles:
            c.keep_inside(w,h)

