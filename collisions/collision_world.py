from vec2 import Vec2
from circle import Circle
from collisions.collision import Collision

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
        self.detect_collision = Collision()

    def update(self,mouse,dt,render):
        for o in self.objs:
            o.update(mouse,dt)
            render.draw_circle(o.pos.x, o.pos.y, o.radius,color='green')
            o.keep_inside(render.w,render.h)

        contacts = []
        for i in range(len(self.objs)):
            for j in range(i+1,len(self.objs)):
                if self.detect_collision.is_collision(self.objs[i],self.objs[j]):
                    contacts.append([self.objs[i],self.objs[j]])

        for o1,o2 in contacts:
            render.draw_circle(o1.pos.x, o1.pos.y, o1.radius,color='red')
            render.draw_circle(o2.pos.x, o2.pos.y, o2.radius, color='red')

