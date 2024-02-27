from tkinter import *
from tkinter.ttk import *
from PIL import ImageGrab
import os

window = Tk()
window.title("Drawing Calculator")
# default size and position
window.geometry("300x325")
# minimum size
window.minsize(225, 250)
# maximum size
window.maxsize(500, 525)

# making the whiteboard window
# subroutines for drawing with pen
def get_coordinates(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y
    relwidth = window.winfo_width()
    my_canvas.create_line((lastx, lasty, event.x, event.y), width=relwidth/15, capstyle=ROUND, smooth=TRUE)

def draw(event):
    global lastx, lasty
    relwidth = window.winfo_width()
    my_canvas.create_line((lastx, lasty, event.x, event.y), width=relwidth/15, capstyle=ROUND, smooth=TRUE)
    lastx, lasty = event.x, event.y

# whiteboard created
my_canvas = Canvas(window, width=300, height=250, bg="white")
my_canvas.pack(fill="both", expand=True)

# Make sure only the part of the window that's visible to user can be drawn on
def OnEnter(event):
    global drawing
    my_canvas.bind('<Button-1>', get_coordinates)
    drawing = my_canvas.bind('<B1-Motion>', draw)

def OnLeave(event):
    try:
        my_canvas.unbind('<Button-1>', drawing)
    except:
        pass
def capture_screenshot():
    global screenshot
    # Get the window's coordinates and dimensions
    x = window.winfo_rootx()
    y = window.winfo_rooty()
    width = window.winfo_width()
    height = window.winfo_height()

    # Temporarily removes the labels
    equation.place_forget()
    equal.place_forget()
    answer.place_forget()
    window.update()

    # Takes the screenshot of the image
    screenshot = ImageGrab.grab(bbox=(2 * x, 2 * y, 2 * (x + width), 2 * (y + height)))

    # Specify the full path including the filename
    save_directory = r"C:\Users\nirva\OneDrive\Documents\screenshots"
    save_path = os.path.join(save_directory, "screenshot.png")

    # Create the directory if it doesn't exist
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # Resize the image to the new resolution
    screenshot = screenshot.resize((28, 28))

    screenshot.save(save_path)
    # readding the labels
    my_canvas.delete('all')
    equation.place(relx=0.35, y=10, anchor='n')
    equal.place(relx=0.50, y=10, anchor='n')
    answer.place(relx=0.60, y=10, anchor='n')

def activate_capture(event=None):
    global after_id
    after_id = window.after(1000, capture_screenshot)

def cancel_capture(event):
    global after_id
    try:
        window.after_cancel(after_id)
    except:
        pass

#Conditons for mouse are set
window.bind('<Button-1>', cancel_capture)
my_canvas.bind('<Enter>', OnEnter)
my_canvas.bind('<Leave>', OnLeave)
window.bind('<ButtonRelease-1>', activate_capture)

# equation produced after input made
# sample holder
equation = Label(window, text="7+8")
equation.place(relx=0.35, y=10, anchor='n')
# label will be constant
equal = Label(window, text="=")
equal.place(relx=0.50, y=10, anchor='n')
# produce result of the equation
answer = Label(window, text="15")
answer.place(relx=0.60, y=10, anchor='n')

# resizes labels based on window size
def on_window_resize(event):
    relwidth = window.winfo_width()
    equation.config(font=("Helvetica", int(relwidth / 15)))
    equal.config(font=("Helvetica", int(relwidth / 15)))
    answer.config(font=("Helvetica", int(relwidth / 15)))

window.bind("<Configure>", on_window_resize)
window.mainloop()
