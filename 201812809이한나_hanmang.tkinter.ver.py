from tkinter import *
import turtle
import random

list=['watermelon', 'chicken', 'greentea', 'cinnamon', 'toothpaste','kimchi', 'lemonade']
sol=random.choice(list)

t=turtle.Turtle()
t.shape("circle")
t.shapesize(1/2)
t.speed(1)
t.ht()
t.up()
t.goto(0,100)

window = Tk()

j=8
def jdg():
    global j
    smp=c.get()
    c.delete(0, END)
    if smp in sol:
        t10.clear()
        t10.write("        있습니다.")
        if j==4:
            j-=1
        turt[j].ht()
        if j>0:
            j-=1
        elif j==0:
            final()
        
    else :
        t10.clear()
        t10.write("        없습니다.")
        attack()
def attack():#전투기들이 내려온다
    global turtle
    x,y = t5.position()
    if y==100 :
        t.st()
        t.goto(0,0)
        t.ht()
        t10.lt(90)
        t10.up()
        t10.goto(0,-1000)
        turtle.bgcolor("black")
        for i in range(10):
            turt[i].reset()
        t10.clear()
        turtle.bgcolor("white")
        t10.write("        게임을 다시 시작하시려면 '다시'를 눌러주세요.")
        e=Button(window, text="다시", command=again)
        e.grid(row=4, column=0)
    else:
        for i in range(9):
            x1,y1=turt[i].position()
            turt[i].goto(x1,y1-20)
def again():
    global j
    j=8
    for i in range(9):
        turt[i].speed(0)
        turt[i].up()
        turt[i].goto(-200+50*i,300)
        turt[i].rt(90)
    t10.shape("turtle")
    t10.shapesize(2)
    t10.lt(90)
    t10.clear()
    d=Button(window, text="확인", command=jdg)
    d.grid(row=3, column=0)
    a=Label(window, text="      알파벳을 쓰세요.     ")
    a.grid(row=0)
def fin():
    smp=c.get()
    c.delete(0, END)
    global sol
    if smp==sol:
        t4.ht()
        t10.clear()
        t10.write("        정답입니다!\n"
                  "        거북이가 신이납니다.")
        t10.up()
        for i in range(50):
            t10.fd(random.randint(0,50))
            t10.lt(random.randint(0,360))
    else :
        t10.clear()
        t10.write("        틀렸습니다.")
        t10.lt(90)
        t10.up()
        t10.goto(0,-1000)
        turtle.bgcolor("black")
        for i in range(10):
            turt[i].reset()
        t10.clear()
        turtle.bgcolor("white")
        t10.write("        게임을 다시 시작하시려면 '다시'를 눌러주세요.")
        e=Button(window, text="다시", command=again)
        e.grid(row=4, column=0)
def final():
    a=Label(window, text="정답은 무엇일까요?(단어)")
    a.grid(row=0, column=0)
    d=Button(window, text="확인", command=fin)
    d.grid(row=3, column=0)

t11=turtle.Turtle()
t11.ht()
t11.up()
t11.speed(0)
t11.goto(-100,-75)
t11.write("암호")
t11.goto(-100,-100)
t11.down()

for i in range(len(sol)):
    for i in range(4):
        t11.fd(15)
        t11.lt(90)
    t11.up()
    t11.fd(25)
    t11.down() 
    
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()
t5=turtle.Turtle()
t6=turtle.Turtle()
t7=turtle.Turtle()
t8=turtle.Turtle()
t9=turtle.Turtle()
t10=turtle.Turtle()
t10.shape("turtle")
t10.shapesize(2)
t10.lt(90)

t10.write("        당신은 거북이를 죽이려는 전투기로부터 거북이를 지킬 수 있습니다.\n"
      "        전투기끼리 송신하는 암호를 맞혀 거북이를 구하세요!")

turt=[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10]

for i in range(9):
    turt[i].speed(0)
    turt[i].up()
    turt[i].goto(-200+50*i,300)
    turt[i].rt(90)

a=Label(window, text="알파벳을 쓰세요.")
a.grid(row=0)

b=Label(window)
b.grid(row=1)

c=Entry(window, bg="white")
c.grid(row=2)

d=Button(window, text="확인", command=jdg)
d.grid(row=3, column=0)

window.mainloop()
