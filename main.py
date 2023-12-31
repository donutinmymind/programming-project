from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Drawing Calculator")
# default size and position
window.geometry("300x325")
# minimum size
window.minsize(225, 250)
# maximum size
window.maxsize(500, 525)
# making the whiteboard window
#subroutines for drawing with pen
def get_coordinates(event):
    global lastx, lasty
    lastx,lasty =event.x, event.y
def draw(event):
    global lastx, lasty
    my_canvas.create_line((lastx, lasty,event.x, event.y),width=12,capstyle=ROUND,smooth=TRUE)
    lastx,lasty=event.x,event.y
#whiteboard created    
my_canvas=Canvas(window,width=300, height=250, bg="white")
my_canvas.pack(fill="both",expand=True)
#Make sure only the part of the window that's visible to user can be drawn on
def OnEnter(event):
    global drawing, coords
    coords=my_canvas.bind('<Button-1>',get_coordinates)
    drawing=my_canvas.bind('<B1-Motion>',draw)
def OnLeave(event):
    try:
        my_canvas.unbind('<Button-1>',drawing)
    except:
        pass
    
my_canvas.bind('<Enter>', OnEnter)
my_canvas.bind('<Leave>',OnLeave)

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
window.mainloop()
