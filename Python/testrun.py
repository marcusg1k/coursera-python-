#fill gaps with nametag function

def nametag(first_name, last_name):
    #ends with .format
    return "{0} {1}.".format(first_name, last_name[0])


print(nametag("Jane", "Smith")) #should output Jane S.
print(nametag("Marcus", "NPC")) #should output Marcus N.
