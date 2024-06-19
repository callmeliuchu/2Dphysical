from circle import Circle
from vec2 import Vec2


class Stick:

    def __init__(self,c1,c2):
        self.c1 = c1
        self.c2 = c2
        self.length = Vec2.length(self.c1.pos,self.c2.pos)

    def keep_length(self):
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



class Cloth:

    def __init__(self,w,h,space=10):
        # c1 = Circle(Vec2(100, 100), 5, 10)
        # c2 = Circle(Vec2(150, 100), 5, 10)
        # c3 = Circle(Vec2(100, 150), 5, 10)
        # c4 = Circle(Vec2(150, 150), 5, 10)
        # self.circles = [c1,c2,c3,c4]
        # s1 = Stick(c1,c2)
        # s2 = Stick(c2,c3)
        # s3 = Stick(c3,c4)
        # s4 = Stick(c4,c1)
        # s5 = Stick(c1,c3)
        # s6 = Stick(c2,c4)
        # self.sticks = [s1,s2,s3,s4,s5,s6]
        self.circles = []
        self.sticks = []

        for y in range(h):
            for x in range(w):
                circle = Circle(Vec2(x*space,y*space),1,10)
                self.circles.append(circle)
                if x != 0:
                    self.sticks.append(Stick(self.circles[-1],self.circles[-2]))
                if y != 0:
                    current = y * w + x - 1
                    last = current - w
                    self.sticks.append(Stick(self.circles[current],self.circles[last]))
                if y == 0 and x % 2 == 0:
                    circle.is_pin = True


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

