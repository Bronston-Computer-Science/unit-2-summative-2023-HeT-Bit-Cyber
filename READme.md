# Summative Assignment Unit 2

### Overview

This Assignment will test your ability to organize and modularize your code. It will require you to utilize and create functions, group those functions in the appropriate modules and then import those modules for use in other files.

### The Scientific Calculator

In this assignment you will build a scientific calculator app using modules and functions. After you completed all the functionalitiy for the app you will then put it all together in a form that's useable and testable by a 3rd party. I will explain each part in detail below.


### Task 1
- create a module called `basic_math.py`
- define the following functions :
- `add` that takes two parameters and returns their sum
- `subtract` that takes two parameters and returns their difference
- `multiply` that takes two parameters and returns their product
- `divide` that takes two parameters and returns their quotient. Be sure to approriately handle division by zero, look in the test modules to figure out what each expected result should be.


### Task 2
- create a module called `trig_calculator.py`
- define the following functions:
- `calculate_sin` that takes an angle in degrees and returns its sine value
- `calculate_cos` that takes an angle in degrees and returns its cosine value.
- `calculate_tan` that takes an angle in degrees and returns its tangent value


### Task 3
- create a module called `unit_conversion.py`
- define the following functions:
- `convert_length` that takes a value in meters and converts it to feet (USE 3.2 as your conversion factor)
- `convert_temperature` that takes a temp in celsuis and converts it to fahrenheit
- `convert_weight` that takes a weight in kilograms and converts it to pounds. (USE 2.2 as your conversion factor)

### Task 4
- create a module called `main.py`
- implement a menu-based interface that allows the users to select different operations:
1. Basic math operations
2. Trigonometric calculations
3. Unit conversions
4. exit

then within each of those selections give them the options to further select which operation that want to execute.
For example the user has selected `1` for Basic math operations, now more options should appear like below
1. add
2. subtract
3. multiply
4. divide
5. exit

### Note!

You should be able to use for loops instead of while loops with break statements. You will be asked this question in the Oral defense portion.

Also when you get the assignment it will be full of errors because I haven't created the files for you. It is your responsibility to make sure you add everything necessary to make sure there are no errors present and the code runs.

This will portion will be auto-graded like the formative. You are encouraged to run the tests your self by typing `pytest` in the terminal to run the test cases