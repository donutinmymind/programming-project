import tkinter
from tkinter import *
window = Tk()
window.title("Drawing Calculator")
# default size and position
window.geometry("300x300+100+100")
# minimum size
window.minsize(200, 200)
# maximum size
window.maxsize(500, 500)
# making the whiteboard border
my_canvas = Canvas(window,width=100, height=100, bg="white")
my_canvas.grid(columnspan=10)
my_canvas.pack(pady=10)
window.mainloop()
