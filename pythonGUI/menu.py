import tkinter as tk
window = tk.Tk()
window.title('my window')
window.geometry('200x200')
l=tk.Label(window,text='',bg='yellow')
l.pack()

counter=0
def do_job():
    global counter
    l.config(text='do'+str(counter))
    counter+=1
#创建菜单
menubar=tk.Menu(window)
#菜单1
filemenu=tk.Menu(menubar,tearoff=0)
#一级菜单
menubar.add_cascade(label='File',menu=filemenu)
#二级菜单
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='OPen',command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.quit)
#菜单二
editmenu=tk.Menu(menubar,tearoff=0)
#一级菜单
menubar.add_cascade(label='edit',menu=editmenu)
#二级菜单
editmenu.add_command(label='cut',command=do_job)
editmenu.add_command(label='paste',command=do_job)
#菜单一子菜单
submenu=tk.Menu(filemenu)
#一级菜单
filemenu.add_cascade(label='Import',menu=submenu,underline=0)
#二级菜单
submenu.add_command(label='Submeaul',command=do_job)
submenu.add_command(label='Submeaul',command=do_job)
window.config(menu=menubar)

#显示出来
window.mainloop()

