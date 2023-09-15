import math
print('Enter option 1 to convert a value from metres to feet')
print('Enter option 2 to convert from temperature in celsuis to fahrenheit')
print('Enter option 3 to convert from kilograms to pounds')
def convert_length():
 print('insert a number')
 number= int(input())
 res1= number*3.2
 print(str(res1)+' Feet')

def convert_temperature():
 print('insert a number')
 num1= int(input())
 res2= (9/5)*num1+32
 print(str(res2)+ 'Fahrenheit')

def convert_weight():
 print('insert a number')
 num1= int(input())
 res3= num1*2.2
 print(str(res3)+ 'Pounds')

opt = int(input("Enter your choice: "))
if opt==1:
 convert_length()
elif opt==2:
 convert_temperature()
elif opt==3:
 convert_weight()
else:
 print('Your option should be within the above choices')