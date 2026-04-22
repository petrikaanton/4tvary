import tkinter as tk
win = tk.Tk()
win.title("halo")
canvas = tk.Canvas(win, width=400, height=400,bg="white")
canvas.pack()
#
#
for i in range(0,11):
    canvas.create_line((i*20,0,200,200),fill="red")
    canvas.create_line((i * 20, 0, 0, 200),fill="blue")
#
#
for i in range(0,6):
    canvas.create_oval((200+(i*20),0+(i*20),400-(i*20),200-(i*20)))
#
#
for y in range(0,9,2):
    for i in range(0,9,2):
        canvas.create_rectangle(((y*20),200+i*20),(20+y*20,220+i*20),fill="pink")
        canvas.create_rectangle(((20+y*20),220+i*20),(40+y*20,240+i*20),fill="pink")
        canvas.create_rectangle(((y*20),220+i*20),(20+y*20,240+i*20),fill="yellow")
        canvas.create_rectangle(((20+y*20),200+i*20),(40+y*20,220+i*20), fill="yellow")
#
#
for i in range(0,11):
    canvas.create_rectangle((200+i*20,200+i*20),(220+i*20,220+i*20),fill="darkgreen")
    canvas.create_rectangle((400-i*20,200+i*20),(380-i*20,220+i*20),fill="yellow")

    #canvas.create_line((0,i*20,200,i*20))
    #canvas.create_line((i*20, 0, i*20, 200))
#
#

win.mainloop()