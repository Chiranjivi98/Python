import mysql.connector

class student:

    def openconn(self):

        self.db=mysql.connector.connect(host='localhost',

                                         user='root',

                                         passwd='',

                                         database='db1')

    def closeconn(self):

        self.db.close()       

    def insert(self):

        self.id=int(input("Enter ID=>"))

        self.name=input("Enter Name=>")

        self.marks=int(input("Enter Marks=>"))

        sql="insert into studinfo values({},'{}',{})".format(self.id,self.name,self.marks)

        cur=self.db.cursor()

        cur.execute(sql)

        self.db.commit()

        if cur.rowcount>0:

            print("Record inserted Successfully!")

    def update(self):

        sql="UPDATE studinfo SET Marks=78 WHERE Marks=57"

        cur=self.db.cursor()

        cur.execute(sql)

        self.db.commit()

        print(cur.rowcount,"Record updated successfully!")

    def delete(self):

        sql="DELETE from studinfo WHERE Marks=78"

        cur=self.db.cursor()

        cur.execute(sql)

        self.db.commit()

        print(cur.rowcount,"Record deleted successfully!")

    def showrec(self):

        sql='select Name from studinfo'

        cur=self.db.cursor()

        cur.execute(sql)

        data=cur.fetchall()

        for i in data:

            print(i)

def main():

    s=student()

    while True:

        print("1-Insert Record\n2-Update Record\n3-Delete Record\n4-Show Record\n5-Exit")

        ch=int(input("Enter your choice=>"))

        if ch==1:

            s.openconn()

            s.insert()

            s.closeconn()

        elif ch==2:

            s.openconn()

            s.update()

            s.closeconn()

        elif ch==3:

            s.openconn()

            s.delete()

            s.closeconn()

        elif ch==4:

            s.openconn()

            s.showrec()

            s.closeconn()

        elif ch==5:

            break

        else:

            print("Invalid Choice!")

main()
