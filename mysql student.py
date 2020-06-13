import mysql.connector



class User:

    def _init_(self):

        pass



    def openconn(self):

        self.db=mysql.connector.connect(host='localhost',user='root',passwd='',database='user')



    def closeconn(self):

        self.db.close()



    def insertdata(self):

        title=input("enter title=>")

        id=input("enter id=>")

        body=input("enter body=>")

        status=input("enter status=>")

        user_id = str(title+id)

        sql="insert into user_info(`title`,`id`,`body`,`status`,`user_id`) values ({},{},{},{},{})".format("'"+title+"'",id,"'"+body+"'","'"+status+"'","'"+user_id+"'")

        print(sql)

        cur=self.db.cursor()

        cur.execute(sql)

        self.db.commit()

        if cur.rowcount>0:

            print("Record inserted Successfully..!")



   

    def showreco(self):

        sql="select * from user_info"

        cur=self.db.cursor()

        cur.execute(sql)

        data=cur.fetchall()

        for i in data:

            print(i[0],i[1],i[2],i[3],i[4])

def main():

    try:

        s=User()

        s.openconn()

        s.insertdata()

        s.showreco()

   

       

    except Exception as e:

        print(e)



    finally:

        s.closeconn()



if _name=='main_':

    main()
