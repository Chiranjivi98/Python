from tkinter.messagebox import *
def save():
    f=open("Information.txt","a+")
    fname=fnametxt.get()
    lname=lnametxt.get()
    g=gender.get()
    s=fname+','+lname+','+g+'\n'
    f.write(s)
    showinfo(title="Save",message="Record Save Succesfully....!")
    print("Record Saved In File")
    f.close()
    
from tkinter import *
#object of window
win=Tk()
win.title("Demo Window")
win.geometry("700x700")

fname=Label(win,text="First Name",bg="yellow",fg="black",font=("arial black",20))
fname.grid(column=0,row=0)
lname=Label(win,text="Last Name",bg="green",fg="black",font=("arial black",20))
lname.grid(column=0,row=1)

fnametxt=Entry(win,width=20,font=("arial black",20))
fnametxt.grid(column=1,row=0)

lnametxt=Entry(win,width=20,font=("arial black",20))
lnametxt.grid(column=1,row=1)

gender=StringVar()
male=Radiobutton(win,text="Male",value="Male",variable=gender,font=("arial black",15),bg="red",fg="blue")
male.grid(column=0,row=3)

female=Radiobutton(win,text="Female",value="Female",variable=gender,font=("arial black",15),bg="red",fg="blue")
female.grid(column=0,row=4)

save=Button(win,text="Save",font=("arial black",15),bg="red",fg="blue",command=save)
save.grid(column=1,row=3)


#infinite loop window till user close it
win.mainloop()
