running_list = [13, 15, 19, 10, 8] 
print(sorted(running_list)) #sorted prints the numbers in order (least to greatest)
print(running_list) #prints list in original order

def greeting(name): 
    print("Welcome, " +name)
result = greeting("Marcus")
print(result) # no return value so the result will print as none

#area of a triangle
def area_triangle(base, height):
    return base*height/2

area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

name = "Marcus" 
number = len(name) * 7
print ("Hello " +name + ". Your lucky number is " + str(number))


name = "Marcus" 
number = len(name) * 7
print ("Hello " +name + ". Your lucky number is " + str(number))
#instead of this
#we can simplify to this
def lucky_number(name):
    number = len(name) *9
    print("Hello " + name + ". Your lucky number is: " + str(number))
    
lucky_number("Marcus")
lucky_number("Npc")

def calculate(d):
    q = 3.14
    z = q * (d ** 2) 
    print(z) 

calculate(5) 

def circle_area(radius): 
    pi = 3.14
    area = pi * (radius ** 2) 
    print(area) 

circle_area(5) 
#output should be the same for both 78.5

# Use a function that accepts mutliple parameters
# return a result value

# This function calculates the number of days in a variable number of 
# years, months, and days. These variables are provided by the user and
# are passed to the function through the function’s parameters.
def find_total_days(years, months, days):
# Assign a variable to hold the calculations for the number of days in
# a year (years*365) plus the number of days in a month (months*30) plus
# the number of days provided through the "days" parameter variable.
    my_days = (years*365) + (months*30) + days
# Use the "return" keyword to send the result of the "my_days"  
# calculation to the function call. 
    return my_days
 
# Function call with user provided parameter values. 
print(find_total_days(2,5,23))


# Use a function to return the result of a measurement conversion
# Use aritmetic operators to perform a calculation
# Combine text with  a funciton call within a print() statement
# Convert the return value from a float data type to a string for the print() function
# Call the function and perform a calculation ont the return value within a print() statement

# This function converts fluid ounces to milliliters and returns the 
# result of the conversion.
def convert_volume(fluid_ounce):
# Calculate value of the "ml" variable using the parameter variable 
# "fluid_ounce". There are approximately 29.5 milliliters in 1 fluid
# ounce.
    ml = fluid_ounce * 29.5  
# Return the result of the calculation.  
    return ml
 
# Call the conversion from within the print() function using 2 fluid 
# ounces. Convert the return value from a float to a string.  
print("The volume in milliliters is " + str(convert_volume(2)))
 
# Call the function again and double the 2 fluid ounces from within
# the print function.
print("The volume in milliliters is " + str(convert_volume(2)*2))
# Alternative calculation:
# print("The volume in milliliters is " + str(convert_volume(4))

# function in the code converts km to meters
# edit code to complete the function so it returns the result
# call the funciton to convert the trip distance from km to meters
# print a text string display the result of the conversion

def convert_distance(km): 
    m = km * 1000
    return m

my_trip_kilometers = 55 
my_trip_meters = convert_distance(my_trip_kilometers)

print("The distance in meters is " + str(my_trip_meters))


#complete the first line of the print_seconds function so that it accepts three paramaters
#hours, minutes and seconds, remember to define a function you use the def keyword

def print_seconds(hours, minutes, seconds):
    print(hours*3600+minutes*60+seconds)
print_seconds(1, 2, 3)
#output is 3723

print(32 == 30+2)   # The == operator checks if the 2 values are 
True                # equal to each other. If they are equal, 
                    # Python returns a True result.


print(5+10 == 6+7)  # If the two values are not equal, as in the
False               # expression 5+10 == 6+7 (or 15 == 13), Python          
                    # returns a False result.


print(10-4 != 10+4) # The != operator checks if the 2 values are
True                # NOT equal to each other. If true, Python              
                    # returns a True result. 


print(9/3 != 3*1)   # In this last example, 9/3 != 3*1 (or 3 != 3)
False               # is false. So, Python returns a False value.

# The = equals assignment operator is used to assign a value to a 
# variable.

my_variable = 3*5           # Assigns a value to my_variable      
print(my_variable)          # Printing the variable returns the 
15                          # value assigned to the variable.


                              
# The == equality comparison operator checks if the values of the two
# expressions on either side of the == operator are equivalent to one 
# another.
      
print(my_variable == 3*5)   # Printing the variable returns a Boolean 
True                        # True or False result. 

# The == operator can check if two strings are equal to each other. 
# If they are equal, the Python interpreter returns a True result.
print("a string" == "a string")
True


# In this example, the equality == comparison is between "4 + 5" and
# 4 + 5. Since the left data type is a string and the right data type
# is an integer, the two values cannot be equal. So, the comparison
# returns a False result.
print("4 + 5" == 4 + 5)
False


# The != operator can check if the two strings are NOT equal to each
# other. If they are indeed not equal, then Python returns a True result.
print("rabbit" != "frog")
True


# In this example, the variable event_city has been assigned the string 
# value "Shanghai". This variable is compared to a static string, 
# "Shanghai", using the != operator. As, the strings "Shanghai" and 
# "Shanghai" are the same, the comparison of "Shanghai" != "Shanghai" 
# is false. Accordingly, Python will return a False result.
event_city = "Shanghai"
print(event_city != "Shanghai")
False

# This last example illustrates the result of trying to compare two
# items of different data types using the equality == operator. The
# two items are not equal, so the comparison returns False.
print("three" == 3)
False

print("matching strings" == "matching strings")
#the interpreter will return a true result
print ("matching strings" != "matching strings")
#interpreter will return a false because the strings are equal
print((6*3 >= 18) and (9+9 <= 36/2))
#interpreter will return a true result
country = "United States" 
city = "New York City" 

print((15/3 < 2+4) or (0 >= 6-7)) 

print(country == "New York City" or city == "New York City")
#false OR true statement so it will return true
x = 2*3 > 6
#returns false bc 6 is not greater than 6
print("The value of x is:")
print(x)

print("")  # Prints a blank line

print("The inverse value of x is:")
print(not x)
#returns false 

today = "Sunday" 
print(not today == "Monday")
#returns true bc sunday is NOT equal to monday
def hint_username(username):
    if len(username) < 3: 
        print("Invalid username. Must be at least 3 characters long.")
    else:
        print("Username successfully created.")

hint_username("Marcus")

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        if len(username) > 15:
            print("Invalid username. Must be at most 15 characters long")
        else:
            print("Valid username")
hint_username("MarcusDriplordAurelius")

print(10*4 > 14+23) 
#prints true because 40 is greater than 37
print("tall" < "short")
#prints false because tall is greater than short (unicode values)


def translate_error_code(error_code):
 
    if error_code == "401 Unauthorized":
        translation = "Server received an unauthenticated request"
 
    elif error_code == "404 Not Found":
        translation = "Requested web page not found on server"
    elif error_code == "408 Request Timeout":
        translation = "Server request to close unused connection"
 
    else:
        translation = "Unknown error code"
    return translation

print(translate_error_code("404 Not Found"))

# Outputs Requested web page not found on server

#quiz conditionals
#1) Whats the value of this Python expression: 
(2**2) == 4
#correct output is true
#2) Complete the script by filling in the missing parts. The function receives a name, then returns a greeting based on whether or not that name is "Taylor".
def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))
#correct
#3) What's the output of this code if number equals 10? 
if number > 11: 
    print(0)
elif number != 10:
    print(1)
elif number >= 20 or number < 12:
    print(2)
else: 
    print(3)
    #output is 2
#4) Is "A dog" smaller or larger than "A mouse"? Is 9999+8888 smaller or larger than 100*100? 
#Replace the plus sign with a comparison operator in the following code to let Python check it for you and then answer. The result should return True if the correct comparison operator is used. 
print("A dog" + "A mouse")
print(9999+8888 + 100*100) 
#5) 
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size * (full_blocks +1)
    return block_size * full_blocks
print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192
#correct

#diegos fav food is lasagna
name = "Diego"
fav_food = "lasagna"
print(name + "'s favorite food is " + fav_food + ".")

print("blue" == "Blue")
#output is false bc strings are not equal

number = 4
if number * 4 < 15:
    print(number / 4)
elif number < 5: 
    print(number + 3)
else:
    print(number * 2 % 5)

#output should be 7 because 4 < 5 and 4 + 3 = 7

#pass fail using if-elif-else statements

def exam_grade(score): 
    if score > 95: 
        return "Top Score"
    elif score >= 60: 
        return "Pass"
    else: 
        grade = "Fail"
        return grade
    
print(exam_grade(65)) # Pass
print(exam_grade(55)) # Fail
print(exam_grade(96)) # Top Score

test_num = 12
if test_num > 15:
    print(test_num / 4) 
else: 
    print(test_num + 3)
#should print 15 bc 12 is not greater than 15

#only supports a,b,c,d, and returns unknown for all other letters or if letter is uppercase
def letter_translator(letter): 
    if letter == "a":
        letter_position = 1
    elif letter == "b": 
        letter_position = 2
    elif letter == "c":
        letter_position = 3
    elif letter == "d": 
        letter_position = 4
    else: 
        letter_position = "unknown" 
    return letter_position
    
print(letter_translator("a"))
print(letter_translator("b"))
print(letter_translator("c"))
print(letter_translator("d"))
print(letter_translator("e"))
print(letter_translator("A"))

#calculate output
def greater_value(x, y):
    if x > y:
        return x
    else: 
        return y
    
print(greater_value(10, 3*5))
#returns 15 because x is not greater than y 

#What's the value of this python expression? 

print((24 == 5*2) and (24 > 3*5) and (2*6 == 12)) 
#should output false

#fill in blanks to complete the safe_division function

def safe_division(numerator, denominator): 
    if denominator == 0: 
        result = 0
    else: 
        result = numerator / denominator
    return result

print(safe_division(5, 5)) #should print 1.0
print(safe_division(5, 4)) #should print 1.25
print(safe_division(5, 0)) #should print 0
print(safe_division(0, 5)) #should print 0.0

#while loop
x = 0 
while x < 5: 
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))
#this prints not there yet 5 times and then prints x = 5

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1 # x = x + 1
    print("Done")

attempts(5)
#prints attempt 1, attempt 2, attempt 3, attempt 4, attempt 5, done
# it keeps incrementing x amount of times until it reaches n

my_variable = 5
while my_variable < 10:
    print("Hello")
    my_variable += 1
# prints hello 5 times

x = 1
sum = 0
while x < 10:
    sum = sum + x
    x = x + 1

product = 1
while x < 10:
    product = product * x
    x = x + 1

print(sum, product)
#Ouput 45 1

def count_down(start_number): 
    current = start_number
    while current > 0: 
        print(current)
        current -= 1
    print("Zero!")
count_down(3)
#outputs 3, 2, 1, zero!

#we want it to stop after 5
def print_range(start, end):
    n = start
    while n <= end:
        print(n)
        n += 1

print_range(1, 5)
# the n += 1 is the incrementer, it broke the infinite loop

multiplier = 1
result = multiplier * 5
while result <= 50:
    print(result)
    multiplier += 1
    result = multiplier * 5
print("Done")
#outputs 5 to 50 in increments of 5

# how can we break this infinite loop
#how can we change the while loop to avoid a python zero division error

def is_power_of_two(number):
    # Check if the number can be divided by two without a remainder
    while number != 0 and number % 2 == 0:
        number = number / 2
    # If after dividing by two the number is 1, it's a power of two
    if number == 1:
        return True
    return False

print(is_power_of_two(0)) # false
print(is_power_of_two(1)) # true
print(is_power_of_two(8)) # true
print(is_power_of_two(9)) # false
#function that takes argument n and returns the sum of the integers

def sum_of_integers(n):
    if n < 1:
        return 0
    
    i = 1
    sum = 0
    while i <= n: 
        sum = sum + i
        i = i + 1

    return sum

print(sum_of_integers(3)) # should print 6
print(sum_of_integers(4)) # should print 10
print(sum_of_integers(5)) # should print 15

#fill in blanks for multiplcation table

def multiplication_table(number): 
    multiplier = 1

    while multiplier <= 10: 
        result = number * multiplier
        if result > 25: 
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result)) 

        multiplier += 1

multiplication_table(3) #should print 3x1=3, 3x2=6, 3x3=9, 3x4=12, 3x5=15
multiplication_table(5)

friends = ['Marcus', 'NPC']
for friend in friends: 
    print("Hi " + friend)

    product = 1
for n in range(1, 10): 
    product = product * n
print(product)
#outputs 362880 because 1*2*3*4*5*6*7*8*9 = 362880

for n in range(5): 
    print(n)
    #outputs 0, 1, 2, 3, 4
    #you want to print "Access Denied" 5 times

for i in range(5): 
    print("Access Denied")

    # you want to print out a sequence of numbers starting at 10 and ending at 30
for i in range(10, 31):
    print(i)
    #outputs the numbers from 10 to 30

    #you want to print out the numbers 20, 19, 18, 17, and 16

i = 20
while(i > 15):
    print(i)
    i = i - 1
    # you want to welcome 3 users from a list by their name

name = ["Marcus", "NPC", "NPC2"]
for i in name: 
    print("Welcome, " , i)

#nested for loops review
for left in range(7):
  for right in range(left, 7):
    print("[" + str(left) + "|" + str(right) + "]", end=" ")
  print()

  teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
  for away_team in teams:
    if home_team != away_team:
      print(home_team + " vs " + away_team)
      
      greeting = 'Hello'
for char in greeting:
	print(char)
#outputs H e l l o but in separate lines
      