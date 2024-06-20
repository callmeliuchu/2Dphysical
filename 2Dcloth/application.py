import tkinter as tk
import random
import time
from vec2 import Vec2
from circle import Circle
from cloth import Cloth
from mouse import Mouse

# circle = Circle(Vec2(100,100),20,10)
# circle.velocity = Vec2(100,100)
force = Vec2(0,2000)

#
# circle.add_force(force)

clo = Cloth(0,0,41,20)
clo.add_force(force)

class DrawingApp:
    def __init__(self, title='Drawing App', width=1200, height=1000):
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


        self.mouse = Mouse()

        # 绑定鼠标左键按下事件
        self.canvas.bind("<Button-1>", self.left_mouse_press)
        # 绑定鼠标右键按下事件
        self.canvas.bind("<Button-2>", self.right_mouse_press)
        # 绑定鼠标左键松开事件
        self.canvas.bind("<ButtonRelease-1>", self.left_mouse_release)
        # 绑定鼠标右键松开事件
        self.canvas.bind("<ButtonRelease-2>", self.right_mouse_release)
        # 绑定鼠标移动事件（按下左键的情况下）
        self.canvas.bind("<B1-Motion>", self.mouse_drag)


        # 启动自动更新
        self.auto_update()

    def left_mouse_press(self, event):
        # 鼠标左键按下事件处理函数
        print("Left button pressed at:", event.x, event.y)
        self.mouse.set_pos(Vec2(event.x, event.y))
        self.mouse.set_click_left(True)

    def right_mouse_press(self, event):
        # 鼠标右键按下事件处理函数
        print("Right button pressed at:", event.x, event.y)
        self.mouse.set_pos(Vec2(event.x, event.y))
        self.mouse.set_click_right(True)

    def left_mouse_release(self, event):
        # 鼠标左键松开事件处理函数
        print("Left button released at:", event.x, event.y)
        self.mouse.set_pos(Vec2(event.x, event.y))
        self.mouse.set_click_left(False)

    def right_mouse_release(self, event):
        # 鼠标右键松开事件处理函数
        print("Right button released at:", event.x, event.y)
        self.mouse.set_pos(Vec2(event.x, event.y))
        self.mouse.set_click_right(False)

    def mouse_drag(self, event):
        # 鼠标移动事件处理函数（按下左键时）
        print("Dragging at:", event.x, event.y)
        self.mouse.set_pos(Vec2(event.x, event.y))

    def draw_circle(self,x,y,radius):
        # 随机位置绘制一个圆
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline='red', width=2)

    def draw_line(self,x0,y0,x1,y1,color='black'):
        self.canvas.create_line(x0,y0,x1,y1,fill=color)

    def auto_update(self):
        # 清空画布
        self.canvas.delete("all")
        # 重新绘制图形
        current_time = time.time()
        dt = current_time - self.last_time



        clo.update(self.mouse,dt)
        # circle.update(dt)
        # circle.keep_inside(self.w,self.h)
        # print(dt,circle.pos.x,circle.pos.y,circle.radius)
        for circle in clo.circles:
            self.draw_circle(circle.pos.x,circle.pos.y,circle.radius)

        for stick in clo.sticks:
            if stick.is_active:
                if stick.is_select:
                    color = 'red'
                else:
                    color = 'black'
                self.draw_line(stick.c1.pos.x,stick.c1.pos.y,stick.c2.pos.x,stick.c2.pos.y,color)

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
