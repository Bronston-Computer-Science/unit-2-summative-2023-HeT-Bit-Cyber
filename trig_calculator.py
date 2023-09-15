import math

def calculate_sin():
    print("INSERT A NUMBER TO CINVERT TO SINE")
    TEMP = int(input())
    ANSWER = TEMP * (22/7)/180
    RESULT= math.sin(ANSWER)
    print(RESULT)

def calculate_cos():
    print("INSERT A NUMBER TO CONVERT TO COSINE")
    TEMP = int(input())
    ANSWER = TEMP* (22/7)/180
    RESULT = math.cos(ANSWER)
    print(RESULT)

def calculate_tan():
    print("INSERT A NUMBER TO CONVERT TO TANGENT")
    TEMP = int(input())
    ANSWER = TEMP * (22/7)/180
    RESULT = math.tan(ANSWER)
    print(RESULT)

print("SELECT OPTION 1 TO FIND SINE")
print("SELECT OPTION 1 TO FIND COSINE")
print("SEECT OPTION 3 TO FINT THE TANGENT")

OPTION = int(input("INSERT YOUR OPTION"))

if OPTION== 1:
    calculate_sin()
elif OPTION == 2:
    calculate_cos()
elif OPTION == 3:
    calculate_tan()
else:
    print("YOUR OPTION SHOULD BE WITHIN NUMBER 1 TO 3")