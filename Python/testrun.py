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
