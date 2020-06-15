#Local and Global Variable
#Use keyword global

f=1000
def abcd():
    global f
    f=9000
    print(f)

def xyz():
    global f
    f=2000
    print(f)
    
print(f)    
abcd()
print(f)
xyz()
'''del f #to delete the variables
print(f)'''
