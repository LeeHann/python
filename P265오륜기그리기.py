import turtle
t=turtle.Turtle()

color=['green','yellow','red']

for i in color:
    t.color(i,i)
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.up()
    t.fd(120)
    t.down()
color=['purple','blue']
t.up()
t.goto(60,-60)
t.down()

for i in color:
    t.color(i,i)
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.up()
    t.fd(120)
    t.down()
