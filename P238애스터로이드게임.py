import turtle
import random
import math

def lt():
    player.lt(30)
def rt():
    player.rt(30)
def play():
    player.fd(3)
    for i in a:
        i.fd(3)
        i.lt(random.randint(-180,180))
    screen.ontimer(play, 10)
    

player=turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.up()
player.speed(0)
screen=turtle.Screen()

screen.onkeypress(lt, "Left")
screen.onkeypress(rt, "Right")                  
screen.listen()

a=[]
for i in range(10):
    a1=turtle.Turtle()
    a1.shape("circle")
    a1.color("red")
    a1.up()
    a1.speed(0)
    a1.goto(random.randint(-300, 300), random.randint(-300,300))
    a.append(a1)
    
screen.ontimer(play, 10)
