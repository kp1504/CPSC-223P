#contacts.py
#By Kshitij Pingle
#16th February, 2024
#This file maintains a dictionary of contacts
#It is also a part of Lab 3 for CPSC 223P

#Note: All data will be maintained in the following manner
#   { id1: ["first1", "last1"], id2: ["first2", "last2"] ... }
#The ids will be phone numbers
#Keys will be ints, Values will be lists


def add_contact(contact_dict, /, *, id1, first_name, last_name):
    """Add a contact to a contact dictionary"""
    
    if (id1 in contact_dict):
        return "error"
    else:
        list1 = [first_name, last_name]
        contact_dict[id1] = list1
        return list1
#End of add_contact function


def modify_contact(contact_dict, /, *, id1, first_name, last_name):
    """Modify an already existing contact in the contact dictionary"""

    #Check if dictionary is empty
    if (len(contact_dict) == 0):        
        return "error"
    elif (id1 not in contact_dict):
        #Key Value pair does not exist to modify
        return "error"
    else:
        list1 = [first_name, last_name]
        contact_dict[id1] = list1
        return list1
#End of modify_contact function


def delete_contact(contact_dict, /, *, id1):
    """Delete a contact with an id in a contact dictionary"""

    #Check if dictionary is empty
    if (len(contact_dict) == 0):
        return "error"
    elif (id1 not in contact_dict):
        return "error"
    else:
        list1 = contact_dict[id1]
        del contact_dict[id1]
        return list1
#End of delete_contact function


def sort_contacts(contact_dict, /):
    """Sort a contact dictionary in ascending order"""

    #Check if contact dict is empty
    if (len(contact_dict) == 0):
        print("Error: dict given to sort_contacts is empty")
        return contact_dict

    else:
        #First sort in ascending order according to last name
        dict2 = dict(sorted(contact_dict.items(), key = lambda x: x[1]))

        #Then sort in ascending order according to first name
        sorted_dict = dict(sorted(dict2.items(), key = lambda x: x[0]))

        return sorted_dict
#End of sort_contacts function


def find_contact(contact_dict, /, *, find):
    """Find a contact in a contact dictionary"""

    dict2 = {}

    if((type(find) == int) and (find in contact_dict)):
        #find is a numeric value and is a key within the contact_dict
        dict2[find] = contact_dict[find]
        return dict2

    else:
        for k, v in contact_dict.items():
            if((find in v[0]) or (find in v[1])):
                #If find is substring of either last or first name
                #Then add it to the new dict
                dict2[k] = v
        if(len(dict2) == 0):
            #Not found
            return dict2
        else:
            #Have found
            sorted_dict = sort_contacts(dict2)
            return sorted_dict
#End of find_contact function


#End of contacts.py











