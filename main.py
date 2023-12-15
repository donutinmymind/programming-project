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
# making the whiteboard window

def get_coordinates(event):
    global lastx, lasty
    lastx,lasty =event.x, event.y
def draw(event):
    global lastx, lasty
    my_canvas.create_line((lastx, lasty,event.x, event.y),width=10,capstyle=ROUND,smooth=TRUE)
    lastx,lasty=event.x,event.y
    
my_canvas=Canvas(window,width=300, height=250, bg="white")
my_canvas.pack(fill="both",expand=True)


my_canvas.bind("<Button-1>",get_coordinates)
my_canvas.bind("<B1-Motion>", draw)
#equation produced after input made
#sample holder
equation = Label(window,text="7+8")
equation.place(relx=0.35,y=10,anchor='n')
#label will be constant
equal = Label(window,text="=")
equal.place(relx=0.50,y=10,anchor='n')
#produce result of the equation
answer = Label(window,text="15")
answer.place(relx=0.60,y=10,anchor='n')
# resizes labels based on window size
def on_window_resize(event):
    relwidth=window.winfo_width()
    equation.config(font=("Helvetica",int(relwidth/15)))
    equal.config(font=("Helvetica",int(relwidth/15)))
    answer.config(font=("Helvetica",int(relwidth/15)))
window.bind("<Configure>",on_window_resize)
window.mainloop
