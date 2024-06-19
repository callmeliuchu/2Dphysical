from vec2 import Vec2

class Circle:

    def __init__(self,pos,radius,mass):
        self.pos = pos
        self.previous = pos
        self.radius = radius
        self.velocity = Vec2(0,0)
        self.force = Vec2(0,0)
        self.mass = mass
        self.is_pin = False
        self.sticks = [None,None]

    def add_force(self,force):
        self.force += force

    def update(self,mouse,dt):
        if self.is_pin:
            return
        dist = Vec2.length(mouse.pos,self.pos)
        for stick in self.sticks:
            if stick:
                stick.is_select = dist < 50 and (mouse.click_left or mouse.click_right)
        acc = self.force / self.mass
        # self.velocity += acc * dt
        # self.pos += self.velocity * dt
        previous = self.pos
        self.pos = self.pos * 2 - self.previous + acc * dt * dt
        self.previous = previous


    def keep_inside(self,w,h):
        if self.pos.x < self.radius:
            self.pos.x = self.radius
            self.velocity.x *= -1

        if self.pos.y < self.radius:
            self.pos.y = self.radius
            self.velocity.y *= -1

        if self.pos.x >= w - self.radius:
            self.pos.x = w - self.radius
            self.velocity.x *= -1

        if self.pos.y >= h - self.radius:
            self.pos.y = h - self.radius
            self.velocity.y *= -1