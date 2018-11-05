from tkinter import *

window = Tk()

#def calculate():

def add():
    global some
    a=eval(blank.get())
    some+=a


some=0
sum=Label(window, text="현재 합계:   %d"%some)
sum.grid(row=0, column=0)

blank=Entry(window, width=20, bg="white")
blank.grid(row=1, column=0, columnspan=3)

plus=Button(window, text="더하기(+)", command=add)
plus.grid(row=2, column=0)
min=Button(window, text="빼기(-)")
min.grid(row=2, column=1)
set=Button(window, text="초기화")
set.grid(row=2, column=2)

window.mainloop()
