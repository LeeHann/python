from tkinter import *

def imge():
    path=inputBox.get()
    img=PhotoImage(file=path)
    imageLabel.configure(image=img)
    imageLabel.image=img

window = Tk()

photo=PhotoImage(file="c:\\Users\\이한나\\Pictures\\박보검.gif")
imageLabel = Label(window, image=photo)
imageLabel.pack()

inputBox = Entry(window)
inputBox.pack()

button = Button(window, text='Submit', command=imge)
button.pack()

window.mainloop()
