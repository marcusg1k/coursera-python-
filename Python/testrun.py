#fill in the blanks to complete the is_palindrome function
# function checks if a string is a palindrome

def is_palindrome(input_string):
    new_string = "" 
    reverse_string = ""
    for letter in input_string:
        if letter != " ": 
            new_string = new_string + letter
            reverse_string = letter + reverse_string

    if new_string.lower() == reverse_string.lower():
        return True
    return False

print(is_palindrome("Never Odd or Even")) # should be true
print(is_palindrome("abc")) # should be false
print(is_palindrome("kayak")) # should be true