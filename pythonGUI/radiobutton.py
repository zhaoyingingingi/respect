import tkinter as tk
window=tk.Tk()
window.title('my winsow')
window.geometry('300x300')

var=tk.StringVar()
l=tk.Label(window,width=20,height=2,text='empty')
l.pack()

def print_selection():
    l.config(text='you have select'+var.get())

r1=tk.Radiobutton(window,text='A',variable=var,value='A',command=print_selection)
r1.pack()

r2=tk.Radiobutton(window,text='B',variable=var,value='B',command=print_selection)
r2.pack()

r3=tk.Radiobutton(window,text='C',variable=var,value='C',command=print_selection)
r3.pack()

r4=tk.Radiobutton(window,text='D',variable=var,value='D',command=print_selection)
r4.pack()


window.mainloop()