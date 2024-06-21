from vec2 import Vec2
from circle import Circle

class World:

    def __init__(self):
        self.objs = []
        force = Vec2(4000, 10000)
        c1 = Circle(Vec2(80,50),100,10)
        c2 = Circle(Vec2(200, 50), 100, 20)
        c1.add_force(force)
        c2.add_force(force)
        self.objs.append(c1)
        self.objs.append(c2)

    def update(self,mouse,dt,render):
        for o in self.objs:
            o.update(mouse,dt)
            render.draw_circle(o.pos.x, o.pos.y, o.radius)
            o.keep_inside(render.w,render.h)
