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

# initial value of the outerloop variable

for outer_loop in range(2, 6+1):
    for inner_loop in range(outer_loop):
        if inner_loop % 2 == 0:
            print(inner_loop)

# the initial value of the outer loop variable is 2
