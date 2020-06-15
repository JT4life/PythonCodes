'''1.CREATE TABLE : EMP : EMPNO , ENAME , SAL  
1 INSERT  
2 UPDATE  
3 DELETE  
4 SELECT  
ENTER YR CHOICE : 1  
    PLEASE ENTER THE VALUE : EMPNO --  
                 ENAME --  
                 SAL --  
    RECORD INSERTED  
                  
ENTER YR CHOICE : 4  
    EMPNO ENAME SAL  
ENTER YR CHOICE : 3       
    ENTER EMPNO FOR DELETE :  
    RECORD DELETED  
      
ENTER YR CHOICE : 3       
-----------------------------------------------------
CREATE FUNCTION :: FNINSERT,FNUPDATE,FNDELETE,FNSELECT
'''  

import sqlite3
connection=sqlite3.connect("employee.db")
cursor = connection.cursor()


    #cursor.execute("Drop table employee;")
sql_command="""
    CREATE TABLE employee(
    empno INTEGER PRIMARY KEY,
    ename VARCHAR(20),
    sal INTEGER);"""

def main():
    while True:
        print("1. Insert")
        print("2. Delete")
        print("3. Update")
        print("4. Select")
        print("5. Exit")

        n=int(input("Enter Your Choice:-->"))
        if n==1:
            insert()
        elif n==2:
            delete()
        elif n==3:
            update()
        elif n==4:
            select()
        else:
            print("Thanks and Welcome!")
            sys.exit()


def insert():#working
    empno = int(input("Enter employee number"))
    ename = input("Enter employee name")
    sal = int(input("Enter employee salary"))
    cursor.execute("insert into employee (empno, ename, sal) VALUES (?,?,?)",(empno,ename,sal))
    connection.commit()
    print("Data Inserted!!!")

def delete():#Working
    ename = input("Enter ename to delete")
    cursor.execute("DELETE from employee where ename=(?)",(ename,))
    cursor.execute("Select * from employee")
    print("fetch all")
    res = cursor.fetchall()
    print(res)
    connection.commit()
    print("Data Deleted!!!")

def update():#working
    p = input("enter 'ename' or 'sal' to update")
    if p == "ename":
        oldEname = input("Enter old ename")
        newEname = input("Enter new ename")
        cursor.execute("UPDATE employee set ename=(?) where ename=(?)",(newEname,oldEname))
        connection.commit()
        print("updated ename!")
    else:
        ename = input("Enter ename of sal you want to update")
        sal = int(input("Enter new employee salary"))
        cursor.execute("UPDATE employee set sal=(?) where ename=(?)",(sal,ename))
        connection.commit()
        print("updated sal!")

def select():#working
    cursor.execute("SELECT * from employee")
    print("fetchall:")
    result = cursor.fetchall()
    for r in result:
        print(r)

if __name__=="__main__":
    main()
