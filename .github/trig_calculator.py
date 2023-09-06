import math

def calculate_sin():
    print("Input a number to convert to sine value")
    degree = int(input())
    result = degree * (22/7)/180
    res2 = math.sin(result)
    print(res2)

def calculate_cos():
    print("Input a number to convert to cosine value")
    degree = int(input())
    result = degree * (22/7)/180
    res2 = math.cos(result)
    print(res2)

def calculate_tan():
    print("Input a number to convert to tangent value")
    degree = int(input())
    result = degree * (22/7)/180
    res2 = math.tan(result)
    print(res2)

print("Select option 1 to find sine value")
print("Select option 2 to find cosine value")
print("Select option 3 to find tangent value")

opt = int(input("Enter your choice: "))

if opt == 1:
    calculate_sin()
elif opt == 2:
    calculate_cos()
elif opt == 3:
    calculate_tan()
else:
    print("Your option should be within 1 to 3")