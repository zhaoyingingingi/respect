# coding=utf-8

import tkinter as tk

window = tk.Tk()
window.title('MyWindow')
window.geometry('400x300')

# 显示的文本
showText = tk.StringVar()

on_hit = False


def on_button_click():
    global on_hit
    if not on_hit:
        on_hit = True
        showText.set('miss you!')
    else:
        on_hit = False
        showText.set('')


# 界面
tk.Label(window, textvariable=showText, bg='green', font=('Arial', 12), width=15, height=2).pack()
tk.Button(window, text='点我', width=15, height=2, command=on_button_click).pack()

window.mainloop()
