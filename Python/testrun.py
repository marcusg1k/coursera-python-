#10) what is the purpose of this following code snippet? 

def generate_report(machines):
    for machine, users in machines.items(): 
        if len(users) > 0: 
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

#chose: purpose of this code is to create a list of all users logged into any machine and the machine theyre logged into