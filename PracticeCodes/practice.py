#Constructor will overload, cannot have multiple
class a:
    def __init__(self):
        print("Default constructor")

    def __init__(self,x=90,n=24):
        print("Constructor passed x=",x,n)
        
    def display(t):
        print("Thanks and welcome")

z = a()
z = a(345)
z = a(22,34)
