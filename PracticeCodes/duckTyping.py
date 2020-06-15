#Duck Typing, whatever is called if its in any class
#it will be called

class pycharm:
    def execute(self):
        print("Good IDE by JetBrains")
    def say(self):
        print("Say hello little friend")
        
class eclipse:
    def execute(self):
        print("Good IDE by Oracle....?")
    def say(self):
        print("Say hi")
        
        
class laptop:
    def a(self, ide):
        ide.execute()
        ide.say()
    
z = pycharm()
x = eclipse()
p = laptop()

p.a(z)
p.a(x)
