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