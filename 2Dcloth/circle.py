from vec2 import Vec2

class Circle:

    def __init__(self,pos,radius,mass):
        self.pos = pos
        self.radius = radius
        self.velocity = Vec2(0,0)
        self.force = Vec2(0,0)
        self.mass = mass

    def add_force(self,force):
        self.force += force

    def update(self,dt):
        acc = self.force / self.mass
        self.velocity += acc * dt
        self.pos += self.velocity * dt

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