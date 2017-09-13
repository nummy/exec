#
#  PSP Assignment 2 (Part II) - Provided module profile.py.
#
#  class Profile
#
#  DO NOT modify this file.
#


class Profile:

    # The __init__ method initializes the data attributes of the Profile class
    def __init__(self, given_name='', family_name='', email='', gender='', status=''):
        self.__given_name = given_name
        self.__family_name = family_name
        self.__email = email
        self.__gender = gender
        self.__status = status
        self.__number_friends = 0
        self.__friends_list = []

    
    def set_given_name(self, name):
        self.__given_name = name
        
    def get_given_name(self):
        return self.__given_name

    def set_family_name(self, name):
        self.__family_name = name

    def get_family_name(self):
        return self.__family_name

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status

    def set_number_friends(self, no_friends):
        self.__number_friends = no_friends

    def get_number_friends(self):
        return self.__number_friends

    def set_friends_list(self, friends_list):
        self.set_number_friends(len(friends_list))
        self.__friends_list = friends_list

    def get_friends_list(self):
        return self.__friends_list


    # The __str__ method returns a string representation of the object
    def __str__(self):
        string = self.__given_name + ' ' + self.__family_name + ' ' + self.__email + ' ' + self.__gender + '\n'
        string += self.__status + '\n'
        string += str(self.__number_friends) + '\n'
        for friend_email in self.get_friends_list():
            string += friend_email + '\n'
        return string


    # The method add_friend adds an email address to the friends_list only if the email doesn't already exist.
    # No duplicate entries allowed.  The method returns True if successful and False otherwise.
    def add_friend(self, email):
      
        # Check to see whether email already exists in the friends list
        if self.is_friend(email) == True:
            return False;

        # Otherwise, okay to add friend and increment number of friends count
        self.__friends_list.append(email)
        self.__number_friends += 1

        return True

    # The method remove_friend removes an email address from the friends_list (if found).
    # Method returns True if successful and False otherwise.
    def remove_friend(self, email):

        # Check to see whether email exists in the friends list
        if self.is_friend(email) == False:
            return False;

        # Otherwise, okay to remove friend and decrement number of friends count
        self.__friends_list.remove(email)
        self.__number_friends -= 1

        return True


    # The method is_friend determines whether the email passed in as a parameter
    # exists in the friends_list, i.e. they are friends.
    # If the email is found in the friends_list, the method will return True.
    # If the email is not found, the function returns False.
    def is_friend(self, email):        
        found = False

        for email_address in self.__friends_list:
            if email == email_address:
                found = True
            
        return found


    # The __eq__ method allows for a test for equality (is equal to) on email address i.e. == operator.
    def __eq__(self, email):
        if self.__email == email:
            return True
        elif self.__email != email:
            return False
        return NotImplemented
     
