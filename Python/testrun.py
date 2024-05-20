#fill in blanks for multiplcation table

def multiplication_table(number): 
    multiplier = 1

    while multiplier <= 10: 
        result = number * multiplier
        if result > 25: 
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result)) 

        multiplier += 1

multiplication_table(3) #should print 3x1=3, 3x2=6, 3x3=9, 3x4=12, 3x5=15
multiplication_table(5)