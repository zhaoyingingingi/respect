import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')
tk.Label(window,text='on the window').pack()

frm=tk.Frame(window,bg='green')
frm.pack()

frm_l=tk.Frame(frm,bg='red')
frm_r=tk.Frame(frm,bg='blue')
frm_l.pack(side='left')
frm_r.pack(side='right')

tk.Label(frm_l,text='1',bg='red').pack()
tk.Label(frm_l,text='2',bg='red').pack()
tk.Label(frm_r,text='3',bg='blue').pack()


window.mainloop()