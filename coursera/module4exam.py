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

#5) fill in to complete the "countries" function
#functions accepts a dictionary containing a list of continents

def countries(countries_dict):
    result = ""

    for continent, countries in countries_dict.items():
        result += continent + ": " + ", ".join(countries) + "\n"
    return result

print(countries({"Africa": ["Nigeria", "Ghana", "Kenya"], "Asia": ["China", "India", "Thailand"]}))

#6) Complete the function so that it accepts a list of people, then iterates over the list and adds all the names
#function should: accept a list variable named "guest_list"
# add the contents of the list as keys to a new, blank dictionary; 
# assign each new key with the value 0; 
# print the new dictionary

def setup_guests(guest_list):
    result = {}
    for guest in guest_list:
        result[guest] = 0
    return result

guests = ["Marcus", "NPC", "NPC2", "NPC3"]

print(setup_guests(guests))

#7) use a dictionary to count the frequency of numbers in the given "text" string
# accept a string "text" variable
#intiliaze an new dictionary
# iterate over each text character to check if the character is a number
# count the frequency of numbers in the input string, ignoring all other characters
# populate the new dictionary with the numbers as keys
# return the new dictionary

def count_numbers(text):
    dictionary = {} 
    for char in text:
        if char.isdigit():
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1
    return dictionary

print(count_numbers("1001000111101"))
#should be {'1': 7, '0': 6}

#8) what do the following commands return when genre = "transcendental"?

genre = "transcendental"
print(genre[:-8]) 
print(genre[-7:9])

#9) What does the list "music_genres" contain after these commands are executed? 


music_genres = ["rock", "pop", "country"]
music_genres.append("blues")

print(music_genres)
#10) What do the following commands return?

host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
print(host_addresses.keys())
