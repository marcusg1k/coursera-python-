#fill in to complete rows_asteriks function

def rows_asteriks(rows): 
    for x in range(0, rows): 
        for y in range(0, x + 1): 
            print("*", end="")
            print()

rows_asteriks(5)

#output should be
#*
#**
#***
#****
#*****