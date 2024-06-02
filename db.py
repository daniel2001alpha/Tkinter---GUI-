import mysql.connector

class Database:
    def __init__(self):
        self.con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Daniel2001",
            database="Employee_Details"
            )
        self.cur=self.con.cursor()
        sql="""
            create table if not exists employee(
                id int not null auto_increment,
                Name varchar(20),
                Age int,
                Date_Of_Joining varchar(12),
                Email varchar(30),
                Gender varchar(15),
                Contact varchar(15),
                Address varchar(100),
                primary key(id)
            )
        """
        self.cur.execute(sql)
        self.con.commit()
        
    #insert Function
    def insert(self,Name,Age,Date_Of_Joining,Email,Gender,Contact,Address):
        sql="insert into employee (Name,Age,Date_Of_Joining,Email,Gender,Contact,Address) values (%s,%s,%s,%s,%s,%s,%s)"
        data=(Name,Age,Date_Of_Joining,Email,Gender,Contact,Address)
        self.cur.execute(sql,data)
        self.con.commit()
        
    #Getting data from DB
    def fetch(self):
        self.cur.execute("select * from employee")
        data=self.cur.fetchall()
        return data

    #Delete data
    def delete(self,Id):
        sql="delete from employee where id=%s"
        self.Id=(Id,)
        self.cur.execute(sql,self.Id)
        self.con.commit()
    #update data
    def update(self,Name,Age,Date_Of_Joining,Email,Gender,Contact,Address,Id):
        self.Id=Id
        sql="update employee set Name=%s,Age=%s,Date_Of_Joining=%s,Email=%s,Gender=%s,Contact=%s,Address=%s where id=%s"
        data=(Name,Age,Date_Of_Joining,Email,Gender,Contact,Address,self.Id)
        self.cur.execute(sql,data)
        self.con.commit()
##o=Database()
####o.insert("Michael",23,"03-11-2019","michael200@gmail.com","Male","9751247569","456 Elm Avenue Somewhere City, Canada Postal Code: A1B 2C3")
####o.fetch()
##o.update("Michael",23,"03-11-2019","michael200@gmail.com","Male","9751247569","Jerusalem City, Israel Postal Code:2C3",2)
##o.fetch()
























