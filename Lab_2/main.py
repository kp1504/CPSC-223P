#main.py
#By Kshitij Pingle
#13th February, 2024
#This file works with contacts.py to maintain a list of employess
#Also, this file is part of Lab 2 for CPSC 233P

#Note:Each list is maintained in the following manner
# [["first1", "last1"], ["first2", "last2"], ...]

from contacts import*
print(dir(contacts.py))

employee_list = [["c", "p"], ["b", "r"], ["a", "q"]]
choice = 0
print("      *** EMPLOYEE CONTACT MAIN MENU")

while True:
    print()
    print("1. Print list")
    print("2. Add contact")
    print("3. Modify contact")
    print("4. Delete contact")
    print("5. Sort list by first name")
    print("6. Sort list by lirst name")
    print("7. Exit the program")
    print()

    #Accept user input for menu choice
    while True:
        try:
            choice = int(input("   Enter menu choice: "))
            if (choice < 1) or (choice > 7):
                print(" Invalid number index. Please enter a number from 1 to 7")
                continue
            else:
                break
        except ValueError:
            print(" Invalid input. Please enter a number from 1 to 7")
            continue

    match choice:
        case 1:
            print_list(employee_list)


        case 2:
            first = input("Enter first name: ")
            last = input("Enter last name: ")
            add_contact(employee_list, first_name = first, last_name = last)


        case 3:
            #Index input error checking
            while True:
                try:
                    index = int(input("Enter index number: "))
                    if ((index < 0) or (index >= len(employee_list))):
                        print("Invalid index. Please enter a number from 0 to", len(employee_list) - 1)
                        continue
                    else:
                        break
                except ValueError:
                    print("Wrong input. you are meant to input a number from 0 to", len(employee_list) - 1)
                    continue
            
            first = input("Enter first name: ")
            last = input("Enter last name: ")
            modify_contact(employee_list, first_name = first, last_name = last, index = index)


        case 4:
            #Index input error checking
            while True:
                try:
                    index = int(input("Enter the index to be deleted: "))
                    if((index < 0) or (index >= len(employee_list))):
                        print("Invalid index. Please enter a number from 0 to", len(employee_list) - 1)
                        continue
                    else:
                        break
                except ValueError:
                    print("Wrong input. you are meant to input a number from 0 to", len(employee_list) - 1)
                    continue
                
            delete_contact(employee_list, index = index)


        case 5:
            #Sort list by first name
            employee_list = sort_contacts(employee_list, column = 0)


        case 6:
            #Sort list by last name
            employee_list = sort_contacts(employee_list, column = 1)

        
        case 7:
            print("Exiting the program now")
            break


        case _:
            print(" Congratulations, you found an error I haven't found yet.")
            print(" Exiting the program now")
            break
