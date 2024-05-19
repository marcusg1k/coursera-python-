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