#Kshitij Pingle
#2nd February, 2024
#Lab 1 for CPSC 223P
#This is the driver file for Lab 1

from contacts import*

#Define a list for use as contact_list
employee_list = []
print("      *** EMPLOYEE CONTACT MAIN MENU")

while True:
    print()
    print("1. Print list")
    print("2. Add contact")
    print("3. Modify contact")
    print("4. Delete contact")
    print("5. Exit the program")
    print()

    #Accept user input for choice
    try:
        choice = int(input("   Enter menu choice: "))
        if (choice < 1) or (choice > 5):
            print(" Invalid number index. Please enter a number from 1 to 5")
            print()
            continue
    except ValueError:
        print(" Invalid input. Please enter a number from 1 to 5")
        continue
    
    match choice:
        case 1:
            print_list(employee_list)

        case 2:
            add_contact(employee_list)

        case 3:
            modify_contact(employee_list)

        case 4:
            delete_contact(employee_list)

        case 5:
            print(" Exiting the program now")
            break

        case _:
            print(" Congratulations, you found an error I haven't found yet.")
            print(" Exiting the program now")

#End of main.py
