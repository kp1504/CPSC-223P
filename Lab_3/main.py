#main.py
#By Kshitij Pingle
#16th February, 2024
#This file is used to interact with a dictionary of contacts
#It is also a part of Lab 3 for CPSC 223P

#Note: All data will be maintained in the following manner
#   { id1: ["first1", "last1"], id2: ["first2", "last2"] ... }
#The ids will be phone numbers
#Keys will be ints, Values will be lists

from contacts import*

employees = {}
choice = 0
print("      *** EMPLOYEE CONTACT MAIN MENU")

while True:

    print()
    print("1. Add contact")
    print("2. Modify contact")
    print("3. Delete contact")
    print("4. Print contact")
    print("5. Find contact")
    print("6. Exit the program")
    print()

    #Accept user input for menu choice
    while True:
        try:
            choice = int(input("Enter menu choice: "))
            print()
            if ((choice < 1) or (choice > 6)):
                print(" Invalid number index. Please enter a number from 1 to 6.")
                continue
            else:
                break
        except ValueError:
            print(" Invalid input. Please enter a number from 1 to 6.")
            continue

    match choice:
        case 1:
            #Add contact
            #Ask for user input
            while True:
                try:
                    phoneno = int(input("Enter phone number: "))
                    break
                except ValueError:
                    print(" Invalid Input. Please enter a number for the phone number.")
                    continue
            first = input("Enter first name: ")
            last = input("Enter last name: ")

            #Call add_contact function
            value = add_contact(employees, id1 = phoneno, first_name = first, last_name = last)

            if (value == "error"):
                print("Phone number already exists.")
            else:
                print("Added:", value[0], value[1], end = "")
                print(".")
        #End of Case 1

        case 2:
            #Modify Contact
            #Check if dict is empty
            if (len(employees) == 0):
                print("The contacts dictionary is currently empty. Please first press 1 to add a contact.")

            else:
                #Get user inputs
                while True:
                    try:
                        phoneno = int(input("Enter a phone number: "))
                        break
                    except ValueError:
                        print(" Invalid input. Please input a number for phone number")
                        continue
                first = input("Enter first name: ")
                last = input("Enter last name: ")

                #Call modify_contact function
                value = modify_contact(employees, id1 = phoneno, first_name = first, last_name = last)

                if(value == "error"):
                    print("Phone number does not exist.")

                else:
                    print("Modified:", value[0], value[1], end = "")
                    print(".")
        #End of Case 2

        case 3:
            #Delete contact list

            #Check if dict is empty
            if (len(employees) == 0):
                print("The contacts dictionary is currently empty. Please first press 1 to add a contact.")


            else:
                #Get user inputs
                while True:
                    try:
                        phoneno = int(input("Enter phone number: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        continue
                
                #Call function to delete
                value = delete_contact(employees, id1 = phoneno)
                if(value == "error"):
                    print("Invalid phone number. The provided phone number does not exist in the contact dictionary.")
                else:
                    print("Deleted:", value[0], value[1], end = "")
                    print(".")
        #End of Case 3
                
        case 4:
            #Print contact list

            if (len(employees) == 0):
                print("The contacts dictionary is currently empty. Please first press 1 to add a contact.")

            else:
                #Print the header
                print()
                print('==================== CONTACT LIST ====================')
                print('Last Name             First Name            Phone')
                print('====================  ====================  ==========')

                for k, v in employees.items():
                    print(f'{v[1]:22}{v[0]:22}{k:10}')
        #End of Case 4

        case 5:
            #Find contact

            #Get user input
            find = input("Enter search string: ")

            #Check if search string is a number
            if (find.isnumeric()):
                find = int(find)
            
            result_dict = find_contact(employees, find = find)

            if(len(result_dict) == 0):
                print("No search results found.")

            else:
                print('================== FOUND CONTACT(S) ==================')
                print('Last Name             First Name            Phone')
                print('====================  ====================  ==========')

                for k, v in result_dict.items():
                    print(f'{v[1]:22}{v[0]:22}{k:10}')
        #End of Case 5

        case 6:
            #Exit program
            print("Exiting program now.")
            break;
        #End of Case 6

        case _:
            #Default case
            print("Congratulations! You found an error that I have not yet.")
            print("Exiting the program now.")
            break;
#End of main.py






            
            
