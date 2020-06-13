from tkinter import *
win=Tk()
win.title('Notepad')
win.geometry('500x500')
#menu in window
mainmenu=Menu(win)
filemenu=Menu(mainmenu)
menu.add_cascade(label='File'.menu="filename")
filename.add_command(label='New')
filename.add_command(label='Open')
filename.add_command(label='Savesfb')






t=Text(win,width='500',height='500')
t.pack()

win.mainloop()
       
