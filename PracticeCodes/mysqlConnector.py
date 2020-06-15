import mysql.connector
connection = mysql.connector.connect(host='localhost',database='jt',user='root',password='Th@0ster')

sqlSelect = "select * from emp"
cursor = connection.cursor()
cursor.execute(sqlSelect)
records = cursor.fetchall()
print("Emp table total", cursor.rowcount)
for row in records:
    print(row)
