#try the enumerate function

def skip_elements(elements):
    new_list = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            new_list.append(element)
    return new_list
        
print(skip_elements(["a", "b", "c", "d", "e", "f",]))
#should output a c e g