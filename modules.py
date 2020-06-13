

from sys import *

f=open('test.txt','r+')

p=input("Enter paragraph=>")

lst=[]

dlist=f.readlines()

plist=p.split()

print(plist)

c=0

for i in plist:

    for j in dlist:

        if j==i:

            break

        else:

            lst.append(i)

            c=c+1

print("incorrect words are",lst)

class FileHandling:

    def __init__(self):

        self.f=open(input("Enter A File Name To Open : "),"w+")

        print(self.f.read())

        self.f.write(input("Enter Something To Write : "))

        self.f.seek(0)

        print(self.f.read())

        self.f.close()



f=FileHandling()

import os

print("Select operation.\n 1. for Read\n 2. for Write\n 3. for Rename\n 4. for Delete\n 5. for Copy\n 6. For Exit")

while True:

    ch= input("Enter Your choice(1/2/3/4/5):")

    if ch in "1":

        f=open("test.txt","r+")

        print(f.read())

        

    if ch in "2":

        f=open("test.txt","w+")

        f.write(input("Enter Something To Write : "))

        f.seek(0)

        print("Write Operation Performed Successfully...!!!")

        print(f.read())



    if ch in "3":

        l=os.listdir()

        print(l)

        a=input("Enter Old File Name : ")

        b=input("Enter New File Name")

        os.rename(a,b)

        print("File Renamed Successfully")

        l1=os.listdir()

        print(l1)



    if ch in "4":

        os.remove(input("Enter File Name or Directory To Remove : "))



    if ch in "5":

        l=os.listdir()

        print(l)

        with open(input("Enter File name for copy"),"r") as og:

            with open(input("Enter File name to copy"),"w") as cp:

                for line in og:

                    cp.write(line)

                    l1=os.listdir()

                    print(l1)

    if ch in "6":

        break


888888888888888888888
with open("test.txt","r") as f:

    with open("out.txt","w") as f1:

        

        for i in f:

            f1.write(i)

