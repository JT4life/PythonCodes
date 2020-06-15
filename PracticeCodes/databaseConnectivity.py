#Database connectivity: Project : 1.Frontend where we design forms/reports
#2. Backend : How to store the data
#SQLITE (Inbuilt database with PYthon)
#SQLite : standalone, RDBMS (light weight)

import sqlite3
'''connection
cursor
execute
commit data
close connection'''

connection=sqlite3.connect("Emp.db") #database 1. if DB is there it will open, 2. if not it creates
cursor = connection.cursor()
cursor.execute("""DROP TABLE employee;""") #table
sql_command="""
CREATE TABLE employee(
staff_number INTEGER PRIMARY KEY,
fname VARCHAR(20),
lname VARCHAR(30),
gender CHAR(1),
joining DATE,
birth_date DATE);"""

cursor.execute(sql_command)
cursor.execute("""INSERT INTO employee (staff_number, fname, lname, gender, birth_date) VALUES (101, "PWilliam", "AShakespeare", "m", "1961-10-25");""")
cursor.execute("""INSERT INTO employee (staff_number, fname, lname, gender, birth_date) VALUES (102, "SWilliam", "WShakespeare", "f", "1961-10-22");""")
cursor.execute("""INSERT INTO employee (staff_number, fname, lname, gender, birth_date) VALUES (103, "AWilliam", "RShakespeare", "m", "1961-1-25");""")
cursor.execute("""INSERT INTO employee (staff_number, fname, lname, gender, birth_date) VALUES (104, "ZWilliam", "TShakespeare", "f", "1961-5-25");""")

connection.commit()
#connection.close()
print("its done")
'''
#2
staff_data = [("William", "Shakespear","m","1961-10-25"),
              ("Frank","Schil","m","1955-11-54"),
               ("Jane","Mar","m","1985-48-45")]

for p in staff_data:
    format_str = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
    VALUES (NULL, "{first}", "{last}", "{gender}", "{birthdate}");"""

    sql_command = format_str.format(first=p[0], last=p[1], gender=p[2], birthdate=p[3])
    cursor.execute(sql_command)

connection.commit()
connection.close()
print("Its done!!!")'''

#3
cursor.execute("SELECT * from employee")
print("fetchall:")
result = cursor.fetchall()
for r in result:
    print(r)

#4
cursor.execute("Select * from employee")
print("\nfetch one:")
res = cursor.fetchone()
print(res)
res = cursor.fetchone() 
print(res)
res = cursor.fetchone() 
print(res)
#Update
'''cursor.execute("UPDATE employee set fname='Joshua' where fname='PWilliam'")
cursor.execute("Select * from employee")
print("fetch all")
res = cursor.fetchall()
print(res)'''

#Delete
cursor.execute("DELETE from employee where fname='Joshua'")
cursor.execute("Select * from employee")
print("fetch all")
res = cursor.fetchall()
print(res)
