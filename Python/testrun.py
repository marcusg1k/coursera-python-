#string slicing

message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message)
#replaces the 3rd character with an "l"