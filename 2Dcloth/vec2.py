class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # 向量加法: (x1, y1) + (x2, y2) = (x1 + x2, y1 + y2)
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        # 向量减法: (x1, y1) - (x2, y2) = (x1 - x2, y1 - y2)
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        # 向量与标量的乘法: k * (x, y) = (k*x, k*y)
        # 这里假设other是标量
        return Vec2(self.x * other, self.y * other)

    def __truediv__(self, other):
        # 向量与标量的除法: (x, y) / k = (x/k, y/k)
        # 这里假设other是标量
        if other != 0:
            return Vec2(self.x / other, self.y / other)
        else:
            raise ValueError("Cannot divide by zero")

    def __repr__(self):
        # 提供一个友好的字符串表示方法
        return f"Vec2({self.x}, {self.y})"

    @classmethod
    def dot(cls,v1,v2):
        return v1.x * v2.x + v1.y * v2.y
