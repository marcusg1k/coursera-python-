# what is the purpose of if len(users) > 0 

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))

# if len(users) > 0 is used to check if the list of users is empty or not
#If the list is not empty, the code inside the if statement will be executed. This helps to avoid printing empty lists or unnecessary information