#public private and protected

class x:
    a=100 #public
    __b=200 # two underscores = private
    _c=400 # single underscore = protected, theres no concept of protected in python
    #but we use single underscore for concept

z = x()
print(z.a)
# print(z.__b) //cant access
print(z._c)

