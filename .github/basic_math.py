import math
print('Select an operation you would like to try')
print('1. To add')
print('2. To subtract')
print('3. To divide')
print('4. To multiply')
operation= int(input())
if operation == 1:
 a=int(input("Enter a number"))
 b=int(input("Enter another number"))
 c=a+b 
 print('Your answer is '+str(c))
if operation == 2:
 a=int(input("Enter a number"))
 b=int(input("Enter another number"))
 c=a-b
 print('Your answer is '+str(c))
if operation == 3:
 a=int(input("Enter a number"))
 b=int(input("Enter another number"))
try: 
    c=a/b
    if b > 0:
        print(c)
    else:
     c= a/b
except ZeroDivisionError:    
    print("Error dividing zero")
if operation == 4:
 a=int(input("Enter a number"))
 b=int(input("Enter another number"))
 c=a*b
 print('Your answer is '+str(c))