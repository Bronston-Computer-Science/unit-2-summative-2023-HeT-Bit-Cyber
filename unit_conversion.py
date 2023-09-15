import math
print('CHOOSE OPTION 1 TO CHANGE FROM METERS TO FEET')
print('CHOOSE OPTION TO CHANGE FROM CELCIUS TO FAHRENHEIT')
print('CHOOSE OPTION 3 TO CHANGE FRON KILOS TO POUNDS')
def convert_length():
 print('INPUT A NUMBER')
 NUMBER= int(input())
 RESULT= NUMBER*3.2
 print(RESULT,"FEET")

def convert_temperature():
 print('INPUT A NUMBER')
 NO1= int(input())
 RESULT2= (9/5)*NO1+32
 print(RESULT2,'FAHRENHEIT')

def convert_weight():
 print('INPUT A NUMBER')
 NO1= int(input())
 RESULT3= NO1*2.2
 print(RESULT3,'POUNDS')

OPTION= int(input("ENTER YOU PREFERED ACTION"))
if OPTION==1:
 convert_length()
elif OPTION==2:
 convert_temperature()
elif OPTION==3:
 convert_weight()
else:
 print('YOUR OPTION SHOULD BE WITHIN NUMBER 1 TO NUMBER 3')