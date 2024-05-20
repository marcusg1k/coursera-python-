#fill in blanks to complete the safe_division function

def safe_division(numerator, denominator): 
    if denominator == 0: 
        result = 0
    else: 
        result = numerator / denominator
    return result

print(safe_division(5, 5)) #should print 1.0
print(safe_division(5, 4)) #should print 1.25
print(safe_division(5, 0)) #should print 0
print(safe_division(0, 5)) #should print 0.0


