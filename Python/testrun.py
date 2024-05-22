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

#function should count how many even numbers exist in a sequence from 0 to the given "n" number
#example even_numbers(25) should return 13

def even_numbers(n): 
    count = 0
    current_number = 0
    while current_number <= n:
        if current_number % 2 == 0:
            count += 1
        current_number += 1
    return count

print(even_numbers(25)) # should output 13
print(even_numbers(144)) # should output 73
print(even_numbers(1000)) # should output 501
print(even_numbers(0)) # should output 1