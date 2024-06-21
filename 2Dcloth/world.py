from vec2 import Vec2
from cloth import Cloth

class World:

    def __init__(self):
        self.objs = []
        force = Vec2(0, 100)
        clo = Cloth(0, 0, 41, 20)
        clo.add_force(force)
        self.objs.append(clo)

    def update(self,mouse,dt,render):
        for clo in self.objs:
            clo.update(mouse,dt)
            for circle in clo.circles:
                render.draw_circle(circle.pos.x,circle.pos.y,circle.radius)
            for stick in clo.sticks:
                if stick.is_active:
                    if stick.is_select:
                        color = 'red'
                    else:
                        color = 'black'
                    render.draw_line(stick.c1.pos.x,stick.c1.pos.y,stick.c2.pos.x,stick.c2.pos.y,color)
            clo.keep_inside(render.w,render.h)


