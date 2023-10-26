import tkinter as tk
window=tk.Tk()
window.title('my window')
window.geometry('300x300')

var1=tk.StringVar()
a=tk.Label(window,bg='yellow',textvariable=var1)
a.pack()

def print_selection():
    value=lb.get(lb.curselection())
    var1.set(value)

b=tk.Button(window,text='print selection',width=15,height=2,command=print_selection)
b.pack()

var2=tk.StringVar()
var2.set((11,22,33,44))

lb=tk.Listbox(window,listvariable=var2)

#创建一个list并将值循环添加到listbox控件
list_item=[1,2,3,4]
for item in list_item:
    lb.insert('end',item)
lb.insert(1,'first')
lb.insert(2,'second')
lb.delete(2)
lb.pack()

window.mainloop()