#1 fill in blanks - correct
#2 find and correct error in the loop - correct
#3 fill in the blanks to complete the function "even_numbers(n)" - wrong
#4 fill in the blanks to complete "rows_Asteriks" - correct
#5 fill in the blanks to complete the "counter" function - wrong
#6 fill in the blanks to complete the even_numbers function - wrong
#7 the sum variable is initliazed with the wrong value = correct
#8 what is the first number printed in the first iteration - 2 (Correct)
#9 initial value of the outer loop - 2 (Correct)
#10 code causes an infinite loop - use for loop (wrong)

#fill in the blanks to complete the "even_numbers" function
#function should return a space separated string of all positive even numbers
#print(even_numbers(6)) #should be 2 4 6

def even_numbers(n):
    return_string = ""
    for x in range(2, n+1, 2):
        return_string += str(x) + " "
    return return_string.strip()
print(even_numbers(6)) # should be 2 4 6
print(even_numbers(10)) # should be 2 4 6 8 10
print(even_numbers(1)) # should be empty
print(even_numbers(3)) # should be 2
print(even_numbers(0)) # should be empty