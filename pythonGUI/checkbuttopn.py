import tkinter as tk
window=tk.Tk()
window.title('my window')
window.geometry('300x300')

l=tk.Label(window,bg='yellow',width=20,height=2,text='empty')
l.pack()

def print_selection():
    if(b1.get()==1)&(b2.get()==0):
        l.config(text="1")
    elif(b1.get()==0)&(b2.get()==0):
        l.config(text="2")
    elif(b1.get()==0)&(b2.get()==0):
        l.config(text="3")
    else:
        l.config(text="4")


b1=tk.IntVar()
b2=tk.IntVar()
c1=tk.Checkbutton(window,text='python',variable=1,onvalue=1,offvalue=0,command=print_selection)
c1.pack()

c2=tk.Checkbutton(window,text='c++',variable=0,onvalue=1,offvalue=0,command=print_selection)
c2.pack()


window.mainloop()