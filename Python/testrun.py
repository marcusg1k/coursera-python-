def biography_list(people): 
    #iterate over each person in the given people list of tuples
    for person in people: 
        #seperate the 3 items in each tuple into 3 variables
        # name, age, and profession
        name, age, profession = person

        #for the required sentence, and place the 3 variables
        # use .format()
        print('{} is {} years old and works as a {}'.format(name, age, profession))


#call to the function
biography_list([('Ira', 30, 'chef'), ('Raj', 35, 'Lawyer'), ('Maria', 25, 'an Engineer')])

# output should match
# Ira is 30 years old and works as a chef
# Raj is 35 years old and works as a Lawyer
# Maria is 25 years old and works as an engineer
