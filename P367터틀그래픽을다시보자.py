import turtle

a=turtle.Turtle()
s=turtle.Turtle()
d=turtle.Turtle()

a.shape("circle")
s.shape("square")
d.shape("turtle")
a.speed(1)
s.speed(1)
d.speed(1)
s.up()
s.goto(0,-20)
s.down()
d.up()
d.goto(0,-40)
d.down()

while True:
    a.circle(50)
    s.circle(70)
    d.circle(90)
