#Kshitij Pingle
#1st February, 2024
#Lab 1 for CPSC 223P
#This file maintains an contact list and has other accessory functions
#such as adding, deleting, modifying, and printing the contact list

#Note: All element lists in contact_list will have the following format
    #["first name", "last name"]

def print_list(contacts):
    """Prints a given contact list"""
    #Show error if list is empty
    if (len(contacts) == 0):
        print(" The contact list is currently empty. Press 2 to first add a contact")
        return contacts
    
    #Print the header
    print()
    print('================== CONTACT LIST ==================')
    print('Index   First Name            Last Name')
    print('======  ====================  ====================')

    #Then iterate through list and print each contact
    contact = 0
    for i in range(len(contacts)):
        print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')
    print()
    return contacts
#End of print_list function


def add_contact(contact_list):
    """Add a contact to a given contact list"""
    element = []
    name = ""
    print("   Adding another contact at index", len(contact_list))
    #Ask for and input first and last name
    #Note:casting input as strings with 'str' keyword
    name = str(input("   Please enter the first name: "))
    element.append(name)
    name = str(input("   Please enter the last name: "))
    element.append(name)
    #Add the ["first name", "last name"] list to contact_list
    contact_list.append(element)
    return contact_list
#End of add_contact function


def modify_contact(contact_list):
    """Modify a contact from the given contact list"""
    #Show error if list is empty
    if (len(contact_list) == 0):
        print("  The contact list is currently empty. Press 2 to first add a contact")
        return contact_list
    
    #Obtaining index from user
    print("   Please enter the contact index number to be modified")
    print("   Note: index should be from 0 to", len(contact_list) - 1, end = "")
    try:
        index = int(input(": "))
        if (index >= len(contact_list)) or (index < 0):
            print()
            print(" Invalid index value.", end = " ")
            print(" Please enter an index from 0 to", len(contact_list) - 1)
            return contact_list
    except ValueError:
        print()
        print(" Invalid input. Please enter a integer for index.")
        return contact_list
    
    #Ask for and input first and last name
    x = str(input("   Please enter the first name: "))
    contact_list[index][0] = x
    x = str(input("   Please enter the last name: "))
    contact_list[index][1] = x
    return contact_list
#End of modify_contact function


def delete_contact(contact_list):
    """Delete an element in a given contact_list"""
    #Show error if list is empty
    if (len(contact_list) == 0):
        print(" The contact list is currently empty. Press 2 to first add a contact")
        return contact_list
    
    #Obtaining index from user
    print("   Please enter the contact index number to be deleted")
    print("   Note: index should be from 0 to", len(contact_list) - 1, end = "")
    try:
        index = int(input(": "))
        if (index >= len(contact_list)) or (index < 0):
            print()
            print(" Invalid index value.", end = " ")
            print(" Please enter an index from 0 to", len(contact_list) - 1)
            return contact_list
    except ValueError:
        print()
        print(" Invalid input. Please enter a integer for index.")
        return contact_list
        
    #Delete the contact from contact_list
    #Note: using the 'del' keyword
    del contact_list[index]
    return contact_list
#End of delete_contact function

#End of contacts.py
