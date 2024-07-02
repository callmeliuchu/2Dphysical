from cloths.circle import Circle
from vec2 import Vec2
from stick import Stick


class Cloth:

    def __init__(self,x_,y_,w,h,space=20):
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
                circle = Circle(Vec2(x_+x*space,y_+y*space),1,10)
                self.circles.append(circle)
                if x != 0:
                    stick = Stick(self.circles[-1],self.circles[-2])
                    self.sticks.append(stick)
                    circle.sticks[0] = stick
                if y != 0:
                    current = y * w + x
                    last = current - w
                    stick = Stick(self.circles[current],self.circles[last])
                    self.sticks.append(stick)
                    circle.sticks[1] = stick
                if y == 0 and x % 2 == 0:
                    circle.is_pin = True


    def add_force(self,force):
        for c in self.circles:
            c.add_force(force)

    def update(self,mouse,dt):
        for c in self.circles:
            c.update(mouse,dt)

        for stick in self.sticks:
            stick.keep_length()


    def keep_inside(self,w,h):
        for c in self.circles:
            c.keep_inside(w,h)

