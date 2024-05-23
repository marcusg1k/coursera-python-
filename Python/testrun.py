#create a function that turns text into pig latin

def pig_latin(text): 
    say = ""

    words = text.split()
    for word in words:
        say += word[1:] + word[0] + "ay "
        return say
    
print(pig_latin("hello how are you"))
print(pig_latin("programming in python is fun"))