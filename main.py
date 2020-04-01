from tkinter import *
speed = 10 #1000 = 1s

pos = 0
def move():
    global pos
    global width
    pos = pos-1
    measure.place(x=pos,y=0)
    print(pos)
    if width < -int(pos) :
      pos = 0  
    measure.after(speed,move)

Window = Tk()
Window.geometry("500x80")


measure = Label(Window, font = ("Arial", 30), text = "Put text here", bg = "black",fg = "orange")
measure.place(x=1,y=1)
measure.update_idletasks()
width = measure.winfo_width()
print(int(width))
move()
