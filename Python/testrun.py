def hint_username(username):
    if len(username) < 3: 
        print("Invalid username. Must be at least 3 characters long.")
    else:
        print("Username successfully created.")

hint_username("Marcus")