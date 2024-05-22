#replace_ending function

def replace_ending(sentence, old, new):
    if sentence.endswith(old):
        i = sentence.rfind(old)
        new_sentence = sentence[:i] + new
        return new_sentence
    
    return sentence

print(replace_ending("It's raining cats and cats", "cats", "dogs"))