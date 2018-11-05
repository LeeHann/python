from turtle import *

class myturtle(Turtle):
    def glow(self, x, y):
        self.fillcolor("red")

turtle=myturtle()
turtle.shape("turtle")
turtle.onclick(turtle.glow)
               
        
