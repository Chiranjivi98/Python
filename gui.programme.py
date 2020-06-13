from tkinter.messagebox import *
def save():
    f=open('information.txt','a+')
    fname1=fnametxt.get()
    lname1=lnametxt.get()
    g=gender.get()
    s=fname1+','+lname1+','+g+'\n'
    f.write(s)
    showinfo(title='Save',message='Record Saved ')
    print('Record Saved ')
    f.close()
    
from tkinter import *
win=Tk()#creates an object of window
win.title('Demo Window')
win.geometry('700x700')
fname=Label(win,bg='white',fg='black',text='First Name',font=('Arial Black',10))
fname.grid(column=0,row=0)
lname=Label(win,bg='white',fg='black',text='Last Name',font=('Arial Black',10))
lname.grid(column=0,row=1)

fnametxt=Entry(win,width=50)
fnametxt.grid(column=1,row=0)
lnametxt=Entry(win,width=50)
lnametxt.grid(column=1,row=1)

gender=StringVar()
male=Radiobutton(win,text='Male',value='male',font=('Arial Black',10),variable=gender)
male.grid(column=0,row=2)
female=Radiobutton(win,text='Female',value='female',font=('Arial Black',10),variable=gender)
female.grid(column=1,row=2)

save=Button(win,text='Save',font=('Arial Black',10),command=save)
save.grid(column=0,row=3)



win.mainloop()#infinite loop open window till user closes it
