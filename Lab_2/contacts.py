#Contacts.py
#By Kshitij Pingle
#13th February, 2024
#This file is used to maintain a list of contacts
#Also, this file is part of Lab 2 for CPSC 233P

#Note: all lists in this function will be in the following format
# [["first1", "last1"], ["first2", "last2"], ...]

def print_list(contacts, /):
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


def add_contact(contact_list, /, *, first_name, last_name):
    """Add a contact to a given list"""
    #Note: first_name and last_name are converted to strings later
    element = [str(first_name), str(last_name)]
    contact_list.append(element)
    #Ask prof if return statment is needed
    return contact_list
#End of add_contact function


def modify_contact(contact_list, /, *, first_name, last_name, index):
    """Modify a contact in a given list"""
    #First, check if list is empty
    if (len(contact_list) <= 0):
        print("The contact_list is currently empty. Press 2 to first add a contact")
        return False
    #Then, check if index is an int
    elif(type(index) != int):
        print("Invalid index argument. Index should be given an int")
        return False
    elif ((index >= len(contact_list)) or (index < 0)):
        print("Invalid index. Index should be from 0 to", len(contact_list) - 1)
        return False
    else:
        contact_list[index][0] = str(first_name)
        contact_list[index][1] = str(last_name)
        return True
#End of modify_contact function


def delete_contact(contact_list, /, *, index):
    """Delete a contact on an index with a given contact list"""
    #Check if list is empty first
    if(len(contact_list) <= 0):
        print("The contact list is currently empty. Press 2 to first add a contact")
        return False
    #Then, check if index is an int
    elif(type(index) != int):
        print("Invalid index argument. Index should be given an int")
        return False
    elif ((index < 0) or (index >= len(contact_list))):
        print("Invalid index. Index should be from 0 to", len(contact_list) - 1)
        return False
    else:
        del contact_list[index]
        return True
#End of delete_contact function


def sort_contacts(contact_list, /, *, column):
    """Sort contacts either according to first or last name"""
    #First, check if list is empty
    if(len(contact_list) <= 1):
        print("The list is too short to be sorted. The list needs to have atleast 2 elements")
        return
    #Then, check if column is not an int
    if(type(column) != int):
        #I'm keeping this check just to let user know column should be an int
            #even though I'm checking if column is 0 or 1 in the next elif
        print("Invalid column argument. Column should be given an int")
        return contact_list
    
    elif((column != 0) and (column != 1)):
        print("Invalid column value. Please give either 0 or 1 for column.")
        #Check if I need to return anything here
        return contact_list
    elif(column == 0):
        #Sort by first_name
        return sorted(contact_list, key = lambda a: a[0])
    elif(column == 1):
        #Sort by last_name
        return sorted(contact_list, key = lambda a: a[1])
#End of sort_contacts function

