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