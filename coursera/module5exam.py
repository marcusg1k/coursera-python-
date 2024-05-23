#1) why is understanding the problem essential to writing a python script?

#2) based on the following code what is the correct output?

numbers = [3, 2, 4, 5, 1] 
numbers.sort()
print(numbers) 
#prints out [1, 2, 3, 4, 5]

#3) which method is used to sort a list and keep the original list intact?
#chose: sorted()

#4) you want to sort the following list in descending order.
# what is the correct code to use to do this?

numbers = [4, 6, 2, 7, 1] 
numbers.sort(reverse=True)
print(numbers)

#5) You need to sort a list of strings based on their length, what argument would you use to do this?

# chose: key=len

#6) Which of the following statements are true about python dictionaries?

#7) Programmer is tasked with developing a program that processes events and prints the associated data to the screen. 
#chose programmer should create one function to process the events and print the associated data to the screen

#8) Which of the following best describes the purpose of an if statement in Python? 
#chose: to execute a block of code only if a certain condition is true

#9) Which of the following statements accurately describes the purpose of an elif statement in python?
#chose: to execute a block of code if a specific condition is true, otherwise execute another block of code

#10) what is the purpose of this following code snippet? 

def generate_report(machines):
    for machine, users in machines.items(): 
        if len(users) > 0: 
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

#chose: purpose of this code is to create a list of all users logged into any machine and the machine theyre logged into