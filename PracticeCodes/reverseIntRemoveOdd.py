#4. 4567 ---> 7654 |456 --->64
n = int(input("Enter a number"))
reverse = 0
number = 0
#while len(str(n))% 2 == 0:
remainder = n % 10
reverse = (reverse * 10) + remainder
number = number / 10
print("Reverse of your number is = ",reverse)
        
