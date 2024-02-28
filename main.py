import tkinter as tk

#!視窗設定
win = tk.Tk()       #建立主視窗
win.title("Note")   #視窗標題
win.geometry('1024x768') #設定視窗長寬('寬x長') > x小寫英文
win.minsize(width=1024,height=768)#設定視窗範圍最小值


win.mainloop()      #常駐主視窗
