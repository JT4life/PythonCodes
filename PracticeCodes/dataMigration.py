from pymongo import MongoClient
import sqlite3
import sys
import mysql.connector
import cx_Oracle


def oracle():#working
    con = cx_Oracle.connect('scott/tiger')
    cur = con.cursor() 
    cur.execute("Select * from emp1")
    for result in cur:
        print(result)
    cur.close()
    con.close()

def mySql():#working
    connection = mysql.connector.connect(host='localhost',database='jt',user='root',password='Th@0ster')
    sqlSelect = "select * from emp1"
    cursor = connection.cursor()
    cursor.execute(sqlSelect)
    records = cursor.fetchall()
    print("Emp1 table total", cursor.rowcount)
    for row in records:
        print(row)

def mysqlInsertMongo():#working
    con=MongoClient("localhost",27017)
    db = con.homework1.emp
    connection = mysql.connector.connect(host='localhost',database='jt',user='root',password='Th@0ster')
    sqlSelect = "select * from emp1"
    cursor = connection.cursor()
    cursor.execute(sqlSelect)
    records = cursor.fetchall()
    print("Emp1 table total", cursor.rowcount)
    for i in records:
        print(i)
        data = {"empno":i[0],"ename":i[1],"salary":i[2]}
        db.insert_one(data)
        connection.commit()
        print("Data inserted into MongoDB")
        
def mongo():#working
    con=MongoClient("localhost",27017)
    db = con.homework1.emp
    cur=db.find()
    for i in cur:
        print(i)

def mongoInsertOracle():#working
    con=MongoClient("localhost",27017)
    db = con.homework1.emp
    connection = cx_Oracle.connect('scott/tiger')
    cursor = connection.cursor() 
    
    mongos = db.find()
    for i in mongos:
        print(str(i["empno"])+" "+i["ename"]+" "+str(i["salary"]))
        cursor.execute("""INSERT INTO emp1(empno,ename,salary) VALUES(:empno,:ename,:salary)""",{"empno":i["empno"],"ename":i["ename"],"salary":i["salary"]})
        connection.commit()
        print("Data from MongoDB has been inserted into Oracle!")
        

def mongoInsertMysql():#working
    con=MongoClient("localhost",27017)
    db = con.homework1.emp
    connection = mysql.connector.connect(host='localhost',database='jt',user='root',password='Th@0ster')
    cursor = connection.cursor()
    
    mongos = db.find()
    for i in mongos:
        print(str(i["empno"])+" "+i["ename"]+" "+str(i["salary"]))
        cursor.execute("""INSERT INTO emp1(empno,ename,salary) VALUES(%s,%s,%s)""",(i["empno"],i["ename"],i["salary"]))
        connection.commit()
        print("Data from MongoDB has been inserted into Mysql!")
    

def mongoInsertSql():#working
    con=MongoClient("localhost",27017)
    db = con.homework1.emp
    conn = sqlite3.connect("homework1.db")
    cursor = conn.cursor()

    mongos = db.find()
    for i in mongos:
        print(str(i["empno"])+" "+i["ename"]+" "+str(i["salary"])) 
        cursor.execute("""INSERT INTO employee(empno,ename,salary) VALUES(?,?,?)""",(i["empno"],i["ename"],i["salary"]))
        conn.commit()
        print("Data from MongoDB has been inserted into Sqlite3!")
    
def sqlite():#working
    conn = sqlite3.connect("homework1.db")
    cursor = conn.cursor()
    '''cursor.execute("Drop table employee;")
    sqlCommand = """CREATE TABLE employee(
        empno INTEGER PRIMARY KEY,
        ename VARCHAR(20),
        salary INTEGER);"""
    cursor.execute(sqlCommand)
    empno = int(input("Enter employee number"))
    ename = input("Enter employee name")
    salary = int(input("Enter employee salary"))
    cursor.execute("insert into employee (empno, ename, salary) VALUES (?,?,?)",(empno,ename,salary))
    conn.commit()
    print("Data Inserted!!!")'''
    cursor.execute("SELECT * from employee")
    print("fetchall:")
    result = cursor.fetchall()
    for r in result:
        print(r)

def sqlInsertMongo():#working
    con=MongoClient("localhost",27017)
    db = con.homework1.emp
    conn = sqlite3.connect("homework1.db")
    cursor = conn.cursor()
    cursor.execute("Select * from employee")
    
    result = cursor.fetchall()
    for i in result:
        print(i)
        data = {"empno":i[0],"ename":i[1],"salary":i[2]}
        db.insert_one(data)
        conn.commit()
        print("Data inserted into MongoDB")

def sqlToMysql():#working
    conn = sqlite3.connect("homework1.db")
    cursor = conn.cursor()
    cursor.execute("Select * from employee")
    connection = mysql.connector.connect(host='localhost',database='jt',user='root',password='Th@0ster')
    cursor2 = connection.cursor()

    result = cursor.fetchall()
    for i in result:
        print(i)
        data = {"empno":i[0],"ename":i[1],"salary":i[2]}
        cursor2.execute("insert into emp1 (empno, ename, salary) VALUES (%s,%s,%s)",(data['empno'],data['ename'],data['salary']))  
        connection.commit()
        print("Inserted data sqlite3 to Mysql")

def sqlToOracle():#not working
    conn = sqlite3.connect("homework1.db")
    cursor = conn.cursor()
    con = cx_Oracle.connect('scott/tiger')
    cur = con.cursor()
    
    result = cursor.fetchall()
    for i in result:
        print(i)
        data = {"empno":i[0],"ename":i[1],"salary":i[2]}
        cur.execute("""INSERT INTO emp1(empno,ename,salary) VALUES(:empno,:ename,:salary)""",{"empno":i["empno"],"ename":i["ename"],"salary":i["salary"]})  
        con.commit()
        print("Inserted data sqlite3 to Oracle")
    
def main():
    while True:
        print("Please select a Database")
        print("1. MongoDB")
        print("2. Sqlite3")
        print("3. Mysql")
        print("4. Oracle")
        print("5. Exit")
        n=int(input("Enter a number to choose:-->"))
        if n==1:
            mongo()
            userInput = int(input("Import data to 1.Sqlite3, 2.Mysql, 3.Oracle, 4.Exit?"))
            if userInput == 1:
                mongoInsertSql()
            elif userInput == 2:
                mongoInsertMysql()
            elif userInput == 3:
                mongoInsertOracle()
            else:
                print("See you next time!")
                sys.exit()
        elif n==2:
            sqlite()
            userInput2 = int(input("Import data to 1.MongoDB, 2.Mysql, 3.Oracle, or 4.Exit?"))
            if userInput2 == 1:
                sqlInsertMongo()
            elif userInput2 == 2:
                sqlToMysql()
            elif userInput2 == 3:
                sqlToOracle()
            else:
                print("See you next time!")
                sys.exit()
        elif n==3:
            mySql()
            userInput3 = int(input("Import data to 1.MongoDB or 2.Exit?"))
            if userInput3 == 1:
                mysqlInsertMongo()
            else:
                print("See you next time!")
                sys.exit()
        elif n==4:
            oracle()
            userInput4 = int(input("Import data to 1.MongoDB or 2.Exit?"))
            if userInput4 == 1:
                mysqlInsertMongo()
            else:
                print("See you next time!")
                sys.exit()    
        else:
            print("See you next time!")
            sys.exit()

        

        


if __name__=="__main__":
    main()
