#Decorators use to change behaviours of functions @compile time
'''
def div(n,m):
    if n < m:
        n,m = m,n
    print(n/m)

#it should swap the value because we want greater value first
#if not we swap the values    
div(2,4)
div(5,20)'''

#nested functions are local to its parent, cannot be called by main
def di(a,b):
    print(a/b)

def smart_di(func):
    def nested(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return nested;

di1 = smart_di(di)
di1(2,20)
