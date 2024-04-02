#main.py
#By Kshitij Pingle
#This file and contacts.py are part of CPSC 223P lab 6

from contacts import *

contact_list = Contacts(filename = "contacts.json")

while True:
    print()
    print("1. Add contact")
    print("2. Modify contact")
    print("3. Delete contact")
    print("4. Print contact")
    print("5. Set contact filename")
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
            #Add a contact
            #Ask for user input
            while True:
                try:
                    phoneno = int(input("Enter phone number: "))
                    break
                except ValueError:
                    print(" Invalid input. Please enter numbers for the phone number.")
                    continue
            first = input("Enter first name: ")
            last = input("Enter last name: ")

            #Ask prof how to check if user just entered twice
            phoneno = str(phoneno)
            #Add the contact
            check = contact_list.add_contact(id = phoneno, first_name = first, last_name = last)

            #Check if error occured
            if (check == "error"):
                print("An error has occured. Please check if the phone number you", end = "")
                print(" entered is already in the contact list.")
                continue

            print("Added:", check[phoneno][0], check[phoneno][1])
        #End of Case 1


        case 2:
            #Modify Contacts

            #Check if contact list is empty
            if (len(contact_list.data) == 0):
                print("The contact list is currently empty. Press 1 to add a contact first")
                continue
            
            #Ask for user input
            while True:
                try:
                    phoneno = int(input("Enter phone number to modify: "))
                    break
                except ValueError:
                    print(" Invalid input. Please enter numbers for the phone number.")
                    continue
            first = input("Enter first name: ")
            last = input("Enter last name: ")

            #Ask prof how to check if user just entered twice
            phoneno = str(phoneno)
            #Modify the contact
            check = contact_list.modify_contact(id = phoneno, first_name = first, last_name = last)

            #Check if error occurred
            if (check == "error"):
                print("An error has occured. Please check if the phone number you", end = "")
                print(" entered is already in the contact list.")
                continue

            print("Modified:", check[phoneno][0], check[phoneno][1])
        #End of Case 2


        case 3:
            #Delete Contact

            #Check if contact list is empty
            if (len(contact_list.data) == 0):
                print("The contact list is currently empty. Press 1 to add a contact first")
                continue
            
            #Ask for user input
            while True:
                try:
                    phoneno = int(input("Enter phone number to delete: "))
                    break
                except ValueError:
                    print(" Invalid input. Please enter numbers for the phone number.")
                    continue

            phoneno = str(phoneno)
            
            #Delete the contact
            check = contact_list.delete_contact(id = phoneno)

            #Check if error occured
            if (check == "error"):
                print("An error has occured. Please ensure the phone number you", end = "")
                print(" entered is in the contact list.")
                continue

            print("deleted:", check[phoneno][0], check[phoneno][1])
        #End of Case 3
            

        case 4:
            #Print contacts

            #Check if contact list is empty
            if (len(contact_list.data) == 0):
                print("The contact list is currently empty. Press 1 to add a contact first")
                continue
            
            x = ''
            #Print the header
            header1 = f'{x:=<21} CONTACT LIST {x:=<21}\n'
            header2 = f'Last Name {x: <13}First Name  {x: <11}Phone\n'
            header3 = f'{x:=<21}  {x:=<21}  {x:=<10}'
            header = header1 + header2 + header3
            print(header)
            for key, value in contact_list.data.items():
                last = value[1]
                first = value[0]
                key1 = key

                entry = f'{last:<21}  {first:<21}  {key1:<10}'
                
                print(entry)
        #End of Case 4


        case 5:
            #Set contact filename
            #Get user input
            filename = input("Please enter the filename: ")

            contact_list = Contacts(filename = filename)
        #End of Case 5
            
        
        case 6:
            #Exit the program
            print("Exiting program now.")
            break;
        #End of Case 6
        

        case _:
            #Default case
            print("Congratulations! You found an error that I have not yet.")
            print("Exiting the program now.")
            break;
        #End of Defualt case
        
#End of main.py
