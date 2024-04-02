#contacts.py
#By Kshitij Pingle
#This file and main.py are part of CPSC 223P Lab 6

import json

class Contacts:
    """A class to make and manage contact lists"""

    #Note:
        #This class uses 'filename' as a variable for filename
        #This class also uses 'data' as the main dictionary

    #The data dicitonary will be as follows:
        #{ "1234" : ["first1", "last1"], "2345" : ["first2", "last2"], ...}

    def __init__(self, /, *, filename):
        self.filename = filename
        self.data = {}              #Make dictionary empty initially
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            #Make a new file if no file exists
            f = open(self.filename, 'x')     #'x' means create a new file
            f.close()
            self.data = {}
        except ValueError:
            #This is to ignore JSONDecode Error which is already handled
            pass
    #End of __init__() method


    def add_contact(self, /, *, id, first_name, last_name):
        """Add a contact to the contact list"""

        id = str(id)
        
        #Check if id is already in dictionary
        if (id in self.data):
            return "error"
        
        elif (id not in self.data):
            #Insert contact into dictionary
            value = list([str(first_name), str(last_name)])
            self.data[id] = value

        #The data dicitonary will be as follows:
            #{ "1234" : ["first1", "last1"], "2345" : ["first2", "last2"], ...}

            #Sort dictionary by last name (ignore case)
            dict1 = dict(sorted(self.data.items(), key = lambda x: x[1][1].lower()))
            
            #Sort dictionary by first name (ignore case)
            dict2 = dict(sorted(dict1.items(), key = lambda x: x[1][0].lower()))

            #Assign sorted dictionary to data
            self.data = dict2

            #Write to file
            try:
                with open(self.filename, 'w') as f:
                    f.write(json.dumps(self.data))
            except FileNotFoundError:
                return "error"
            
            #Return key:value pair  Ask prof to check this
            return {id : value}
    #End of add_contact function


    def modify_contact(self, /, *, id, first_name, last_name):
        """Modify a contact in the contact list"""

        id = str(id)
        
        #Check if id is in dictionary
        if (id not in self.data):
            print("\nDEBUG: not in data dictionary\n")
            print(self.data)
            return "error"
            
        else:
            value = [first_name, last_name]
            self.data[id] = value

        #The data dicitonary will be as follows:
            #{ "1234" : ["first1", "last1"], "2345" : ["first2", "last2"], ...}
    
            #Sort dictionary by last name (ignore case)
            dict1 = dict(sorted(self.data.items(), key = lambda x: x[1][1].lower()))
            
            #Sort dictionary by first name (ignore case)
            dict2 = dict(sorted(dict1.items(), key = lambda x: x[1][0].lower()))

            #Assign sorted dictionary to data
            self.data = dict2

            #Write to data dictionary
            try:
                with open(self.filename, 'w') as f:
                    f.write(json.dumps(self.data))
            except FileNotFoundError:
                return "error"

            #Return key:value pair  Ask prof to check this
            return {id : value}
    #End of modify_contact function


    def delete_contact(self, /, *, id):
        """Delete a contact in the contact list"""

        id = str(id)
        
        #Check if data dict is empty or if id is not in dictionary
        if ((len(self.data) == 0) or (id not in self.data)):
            return "error"
        else:
            value = self.data[id]
            del self.data[id]

            #Write changes to file
            try:
                with open(self.filename, 'w') as f:
                    f.write(json.dumps(self.data))
            except FileNotFoundError:
                return "error"

            #Return key:value pair  Ask prof to check this
            return {id : value}
    #End of delete_contact function
#End of Contacts Class and contacts.py
