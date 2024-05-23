#lets use tuples to store information

def file_size(file_info):
    name, type, size = file_info
    return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875)))