import cx_Oracle
con = cx_Oracle.connect('scott/tiger')
cur = con.cursor()
cur.execute("Insert into yang values('john',555)")
cur.execute("Insert into yang values('thor',666)")
cur.execute("Insert into yang values('hulk',7777)")
'''cur.execute("Delete from yang where ename='john'")'''
cur.execute("Select * from yang")
for result in cur:
    print(result)
cur.close()
con.close()
