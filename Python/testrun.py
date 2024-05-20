#we want it to stop after 5
def print_range(start, end):
    n = start
    while n <= end:
        print(n)
        n += 1

print_range(1, 5)
# the n += 1 is the incrementer, it broke the infinite loop
