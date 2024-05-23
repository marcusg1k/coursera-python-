#fill in, using list comprehension

def odd_numbers(n):
    return [x for x in range(1, n+1) if x % 2 != 0]

print(odd_numbers(5))
print(odd_numbers(10))
print(odd_numbers(11))
print(odd_numbers(1))
print(odd_numbers(-1))