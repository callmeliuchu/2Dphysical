import tkinter as tk
import random
import time
from vec2 import Vec2
from circle import Circle
from cloth import Cloth

# circle = Circle(Vec2(100,100),20,10)
# circle.velocity = Vec2(100,100)
force = Vec2(10,1500)

#
# circle.add_force(force)

clo = Cloth(50,100,41,20)
clo.add_force(force)

class DrawingApp:
    def __init__(self, title='Drawing App', width=500, height=500):
        # 初始化主窗口
        self.w = width
        self.h = height
        self.root = tk.Tk()
        self.root.title(title)

        # 设置画布
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg='white')
        self.canvas.pack()

        # # 在画布上绘制图形
        # self.draw_shapes()
        self.last_time = time.time()

        # 启动自动更新
        self.auto_update()

        # 绑定鼠标点击事件
        self.canvas.bind("<Button-1>", self.mouse_click)

        # 绑定鼠标移动事件（按下左键的情况下）
        self.canvas.bind("<B1-Motion>", self.mouse_drag)

    def mouse_click(self, event):
        # 鼠标点击事件处理函数
        print("Clicked at:", event.x, event.y)

    def mouse_drag(self, event):
        # 鼠标移动事件处理函数
        print("Dragging at:", event.x, event.y)

    def draw_circle(self,x,y,radius):
        # 随机位置绘制一个圆
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline='red', width=2)

    def draw_line(self,x0,y0,x1,y1):
        self.canvas.create_line(x0,y0,x1,y1)

    def auto_update(self):
        # 清空画布
        self.canvas.delete("all")
        # 重新绘制图形
        current_time = time.time()
        dt = current_time - self.last_time

        clo.update(dt)
        # circle.update(dt)
        # circle.keep_inside(self.w,self.h)
        # print(dt,circle.pos.x,circle.pos.y,circle.radius)
        for circle in clo.circles:
            self.draw_circle(circle.pos.x,circle.pos.y,circle.radius)

        for stick in clo.sticks:
            self.draw_line(stick.c1.pos.x,stick.c1.pos.y,stick.c2.pos.x,stick.c2.pos.y)

        clo.keep_inside(self.w,self.h)
        self.last_time = current_time
        # 每秒自动更新一次
        self.root.after(10, self.auto_update)

    def run(self):
        # 启动程序
        self.root.mainloop()


if __name__ == "__main__":
    app = DrawingApp()
    app.run()
