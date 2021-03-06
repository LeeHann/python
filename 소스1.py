from tkinter import *
import time
import random

color_list=["blue","red","pink","white","silver","skyblue"]
ball_list=[]

window=Tk()
canvas=Canvas(window, width=800, height=400)
canvas.pack()

class Ball:
    def __init__(self, canvas, color, size, x,y, xspeed, yspeed):
        self.canvas=canvas
        self.color=color
        self.size=size
        self.x=x
        self.y=y
        self.xspeed=xspeed
        self.yspeed=yspeed
        self.id=canvas.create_oval(x,y,x+size, y+size, fill=color)

    def move(self):
        self.canvas.move(self.id, self.xspeed, self.yspeed)
        (x1,y1,x2,y2)=self.canvas.coords(self.id)
        (self.x,self.y)=x1,y1
        if x1<=0 or x2>=800:
            self.xspeed=-self.xspeed
        if y1<=0 or y2>400:
            self.yspeed=-self.yspeed
for i in range(10):
    color=random.choice(color_list)
    size=random.randint(10,100)
    xspeed=random.randint(1,10)
    yspeed=random.randint(1,10)
    ball_list.append(Ball(canvas, color, size, 0,0,xspeed,yspeed))

while True:
    for ball in ball_list:
        ball.move()
    window.update()
    time.sleep(0.03)

window.mainloop()
