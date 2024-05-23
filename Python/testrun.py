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