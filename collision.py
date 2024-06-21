from circle import Circle


class Collision:

    def __init__(self):
        pass

    def is_collision(self,a,b):
        if isinstance(a,Circle) and isinstance(b,Circle):
            return self.circle_circle(a,b)
        return  True


    def circle_circle(self,a,b):
        ab_length = (a.pos-b.pos).mag()
        ab = a.radius + b.radius
        return ab > ab_length

    def circle_polygon(self,a,b):
        pass

    def polygon_polygon(self,a,b):
        pass