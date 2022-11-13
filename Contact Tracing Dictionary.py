# Create Dictionary
contact_dictionary = {}
# Display Menu
while True:
    print("\nMenu")
    print("1 -> Add an item")
    print("2 -> Search")
    print("3 -> Exit (y/n)")
    # Input user choice
    choice = int(input("\nWhat do you want to do? (1-3): "))
    # Option 1 Result
    if choice == 1:
        name = input("\nName: ")
        gender = input("Gender: ")
        age = input("Age: ")
        address = input("Address: ")
        number = input("Phone Number: ")
        print("\nSaved!!")
        contact_dictionary[name] = [gender, age, address, number]
    # Option 2 Result
    elif choice == 2:
        search_name = input("Name: ")
        if search_name in contact_dictionary:
            print("Here is the information!! (Gender/Age/Address/Phone Number)\n",
                  contact_dictionary[search_name])
        else:
            print("We could not find your name in the list! Try Again!")
    # Option 3 Result
    elif choice == 3:
        print("Thank you for using contact tracing!")
        break
