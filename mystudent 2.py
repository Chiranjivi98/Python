import mysql.connector



class student:



    def openconn(self):



        self.db=mysql.connector.connect(host='localhost',



                                         user='root',



                                         passwd='',



                                         database='py1')



    def closeconn(self):



        self.db.close()       



    def insert(self):



        self.id=int(input("Enter ID=>"))



        self.name=input("Enter Name=>")



        self.rank=int(input("Enter Rank=>"))



        sql="insert into studin values({},'{}',{})".format(self.id,self.name,self.rank)



        cur=self.db.cursor()



        cur.execute(sql)



        self.db.commit()



        if cur.rowcount>0:



            print("Record inserted Successfully!")



    def search(self):

        self.search=input("Enter the name you want to search=>")

        if self.search==self.name:

            print("Record found successfully!")

        else:

            print("Record not Found!")



def main():

    while True:

        s=student()

        s.openconn()

        s.insert()

        s.closeconn()

        print("Do you want to continue?......(Y/N)")

        ch=input("Enter your choice=>")

        if ch=='Y':

            continue

        elif ch=='N':

            break



    print("Do u want to search record by name?....(y/n)")

    ch1=input("Enter the choice=>")

    if ch1=='y':

        s.openconn()

        s.search()

        s.closeconn()

    else:

        print("Invalid Choice!")



main()
