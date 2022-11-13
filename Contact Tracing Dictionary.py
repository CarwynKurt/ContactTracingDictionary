# Create Dictionary
contact_dictionary = {}
# Display Menu
print("Menu")
print("1 -> Add an item")
print("2 -> Search")
print("3 -> Exit (y/n)")
# Input user choice
choice = int(input("What do you want to do? (1-3): "))
# Option 1 Result
if choice == 1:
    name = input("Name: ")
    gender = input("Gender: ")
    age = input("Age: ")
    address = input("Address: ")
    number = input("Phone Number: ")
    print("Saved!!")
    contact_dictionary = {name : [gender, age, address, number]}
    print(contact_dictionary)
# Option 2 Result
# Option 3 Result
# Loop