# 1) fill in to complete the "confirm_length" function
#function should return how many characters a string contains as long as it has one or more characters

def confirm_length(word):
    if len(word) > 0: 
        return len(word)
    else: 
        return 0
    
print(confirm_length("a")) #should print 1
print(confirm_length("marcus")) #should print 6

#2) fill in the blank to complete the "highlight_word" function
# this function should change the given "word" to uppercase

def highlight_word(sentence, word):
    return sentence.replace(word, word.upper())

print(highlight_word("Have a great day", "nice")) 
# should print Have a NICE day

#3) Complete the code to combine the two lists into one in the order of: the contents of Drew's list
# followed by Jaime's list in reverse order
# function should accept 2 lists, reverse the order of "list1"; 
# combine the two lists so that list2 comes first, followed by list1
# return the new list

def combine_list(list1, list2): 
    
#initialize an empty list var
# reverse the order of list1
#combine the two lists

    combined_list = []
    list1.reverse()
    combined_list = list2 + list1
    return combined_list

Jaimes_list = ["Alma", "Chika", "Benjamin"]
Drews_list = ["Drew", "Eli", "Finn"]

print(combine_list(Jaimes_list, Drews_list))

#4) Fill in the blank to complete the "squares function"
# using either n*n or n**2

def squares(start, end): 
    return [n**2 for n in range(start, end+1)]

print(squares(2, 3)) #should print [4, 9]
print(squares(1, 5)) #should print [1, 4, 9, 16, 25]