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

#complete the countdown function
#function should begin at the start variable 
#function call like countdown(2) will return 2, 1, 0

def countdown(start):
    x = start
    if x > 0:
        return_string = "Counting down to 0: "
        while x >= 0: 
            return_string += str(x)
            if x > 0:
                return_string += ", "
            x -= 1
    else: 
        return_string = "Cannot count down to 0"
    return return_string

print(countdown(10))
print(countdown(2))
print(countdown(0))
