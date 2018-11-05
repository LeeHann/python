import turtle
t11=turtle.Turtle()          #, 'chicken', 'greentea', 'cinnamon', 'toothpaste','kimchi', 'lemonade'
sol='watermelon'
smp='w'
t11.ht()
def alpabet():
    if sol=='watermelon':
        if smp=='w':
            t11.up()
            t11.goto(-200, -195)
            t11.write('w')
        if smp==a:
            t11.up()
            t11.goto(-175, -195)
            t11.write('a')
        if smp==t:
            t11.up()
            t11.goto(-150, -195)
            t11.write('t')
        if smp==e:
            t11.up()
            t11.goto(-125, -195)
            t11.write('e')
            t11.up()
            t11.goto(-50, -195)
            t11.write('e')
        if smp==r:
            t11.up()
            t11.goto(-100, -195)
            t11.write('r')
        if smp==m:
            t11.up()
            t11.goto(-75, -195)
            t11.write('m')
        if smp==l:
            t11.up()
            t11.goto(-25, -195)
            t11.write('l')
        if smp==o:
            t11.up()
            t11.goto(0, -195)
            t11.write('o')
        if smp==n:
            t11.up()
            t11.goto(25, -195)
            t11.write('n')
    if sol==chicken:
        if smp==w:
            t11.up()
            t11.goto(-200, -195)
            t11.write('w')
        if smp==a:
            t11.up()
            t11.goto(-175, -195)
            t11.write('a')
        if smp==t:
            t11.up()
            t11.goto(-150, -195)
            t11.write('t')
        if smp==e:
            t11.up()
            t11.goto(-125, -195)
            t11.write('e')
            t11.up()
            t11.goto(-50, -195)
            t11.write('e')
        if smp==r:
            t11.up()
            t11.goto(-100, -195)
            t11.write('r')
        if smp==m:
            t11.up()
            t11.goto(-75, -195)
            t11.write('m')
        if smp==l:
            t11.up()
            t11.goto(-25, -195)
            t11.write('l')
        if smp==o:
            t11.up()
            t11.goto(0, -195)
            t11.write('o')
        if smp==n:
            t11.up()
            t11.goto(25, -195)
            t11.write('n')
alpabet()
t11=turtle.Turtle()
t11.ht()
t11.up()

t11.goto(-200,-100)
t11.down()
for i in range(len(sol)):
    t11.fd(15)
    t11.up()
    t11.fd(10)
    t11.down() 
