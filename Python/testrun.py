filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
#gererate new filenames as a list containing the new filenames

new_filenames = []
for filename in filenames:
    if filename.endswith(".hpp"):
        new_filenames.append(filename[:-2])
    elif filename.endswith(".h"):
        new_filenames.append(filename[:-1])
    else:
        new_filenames.append(filename)
print(new_filenames)
#should print ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]