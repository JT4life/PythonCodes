#Stack : Last in first out data structure
#Using list : in the list push, append, pop

stack=[]
print("\n Current Stack",stack)
print("\n Push Items in Stack")

for i in range(5):
    stack.append(i)
print(stack)
print("Current stack size is ",len(stack))

print("\nPop Items from stack")
while len(stack) > 0:
    stack.pop()
    print(stack)
    print("\nCurrent stack size is -->", len(stack))

