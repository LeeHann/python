from turtle import*

class Car:
    def __init__(self, speed, color, model):
        self.speed=speed
        self.color=color
        self.model=model
        self.turtle=Turtle()
        self.turtle.shape("C:\\Users\\이한나\\Desktop\\car.gif")
        
    def drive(self):
        self.turtle.fd(self.speed)
        
    def left_turn(self):
        self.turtle.left(90)

register_shape("C:\\Users\\이한나\\Desktop\\car.gif")    
myCar=Car(0, "blue","E-class")

for i in range(100):
    myCar.drive()
    myCar.left_turn()
