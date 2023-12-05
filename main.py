from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Drawing Calculator")
# default size and position
window.geometry("300x300")
# minimum size
window.minsize(200, 200)
# maximum size
window.maxsize(500, 500)
# making the whiteboard border
my_canvas = Canvas(window,width=300, height=250, bg="white")
#equation produced after input made
#sample holder
equation = Label(window,text="7+8")
equation.place(x=140,y=10)
#label will be constant
equal = Label(window,text="=")
equal.place(x=180,y=10)
#produce result of the equation
equation = Label(window,text="15")
equation.place(x=200,y=10)
my_canvas.place(x=0,y=50)
window.mainloop
