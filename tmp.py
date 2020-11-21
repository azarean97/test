import tkinter as tk
from tkinter import StringVar

root = tk.Tk(baseName='main', className='mainWindows')
canvas = tk.Canvas(root, height=500, width=700)
canvas.pack()

def buttonfun (a):
    if a==1:
        return('yes')
    else:
        return('no')
# bgImgMain = tk.PhotoImage(file = '/home/ali/Desktop/game.jpg')
# bgImg = tk.Label(root,image=bgImgMain)
# bgImg.place()


mainFrame = tk.Frame(root, bg='#333333')
frame1 = tk.Frame(root, bg='#80c1ff', bd=5)
frame2 = tk.Frame(root, bg='#80c1ff', bd=5)

mainFrame.place(relwidth=1, relheight=1)
frame1.place(relx=0.13, rely=0.1, relwidth=0.75, relheight=0.1)
frame2.place(relx=0.13, rely=0.3, relwidth=0.75, relheight=0.55)


button = tk.Button(frame1, text='get Weather', font=32,command=lambda:buttonfun(entry.get()))
button.place(relwidth=0.25, relheight=1, relx=.75)

entry = tk.Entry(frame1)
entry.place(relwidth=0.7, relheight=1)


label = tk.Entry(frame2)
label.insert(0,buttonfun(entry.get()))
# label['text'] = buttonfun(entry.get())

label.pack(fill='both', expand=True)

root.mainloop()
