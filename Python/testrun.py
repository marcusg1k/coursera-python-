#use format method to fill gaps in the convert_distance function

def convert_distance(miles):
    km = miles * 1.6
    result = "{miles} miles equals {km} km".format(miles=miles, km=km)
    return result

print(convert_distance(12)) #should be 12 miles equals 19.2 km
print(convert_distance(5.5)) #should be 5.5 miles equals 8.8 km
print(convert_distance(11)) #should be 11 miles equals 17.6 km