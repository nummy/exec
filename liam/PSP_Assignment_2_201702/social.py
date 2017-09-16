#
# File : fileName.py
# Author : your name
# Saibt Id : your saibt id
# Description : Assignment 2   place assignment description here . . .
# This is my own work as defined by the University ’s
# Academic Misconduct pol icy .
#

import profile
import list_function 


# Function read_file() - read file and get profiles into profile_list
def read_file(filename, profile_list):
    fp = open(filename, "r")
    data_lst = fp.readlines()
    counter = 0
    while counter < list_function.length(data_lst):
        data = data_lst[counter]
        counter += 1
        gname, fname, email, gender = data.strip().split()  # get basic info
        status = data_lst[counter].strip()  # get status
        counter += 1
        num = int(data_lst[counter].strip())  # get friend num
        counter += 1
        friends = []
        for index in range(num):
            # get friend list
            friends.append(data_lst[counter].strip())
            counter += 1
        person = profile.Profile(gname, fname, email, gender, status)
        person.set_number_friends(num)
        person.set_friends_list(friends)
        profile_list.append(person) # append a person


# Function display_summary() - dispay summary information of the profiles
def display_summary(profile_list):
    print("==============================================================================")
    print("Profile Summary")
    print("==============================================================================")
    for person in profile_list:
        print("--------------------------")
        output = "{} {} ({} | {})\n- {}\n".format(person.get_given_name(), person.get_family_name(), 
            person.get_gender(), person.get_email(), person.get_status())
        num = person.get_number_friends()
        # if no friends
        if num == 0:
            output += "- No friends yet..."
        else:
            # with friends
            output += "- Friends ({}):\n".format(num)
            friends = person.get_friends_list()
            length = list_function.length(friends)
            for i in range(0, length):
                email = profile_list[find_profile(profile_list, friends[i])].get_email()
                if i != length - 1:
                    # handle the last one 
                    output += "    " + email + "\n"
                else:
                    output += "    " +  email
        print(output)
    print("--------------------------")
    print("==============================================================================")

# Function write_to_file() - write profile list to file
def write_to_file(filename, profile_list):
    output = open(filename, "w")
    for person in profile_list:
        output.write(str(person))

# Function find_profile() - find the person by email
def find_profile(profile_list, email):
    length = list_function.length(profile_list)
    for index in range(length):
        if profile_list[index].get_email() == email:
            return index
    return -1

# Function add_profile() - add a new profile
def add_profile(profile_list):
    email = input("Please enter email address: ")
    if find_profile(profile_list, email) > 0:
        # if exists
        print("{} already exists in profiles".format(email))
    else:
        # add new profile
        gname = input("Please enter given name: ")
        fname = input("Please enter family name: ")
        gender = input("Please enter gender: ")
        status = input("Please enter current status: ")
        person = profile.Profile(gname, fname, email, gender, status)
        profile_list.append(person)
        print("Successfully added {} to profiles.".format(email))
    return profile_list


# Function remove_profile() - remove profile by email
def remove_profile(profile_list):
    email = input("Please enter email address: ")
    index = find_profile(profile_list, email)
    if index > 0:
        # if found
        profile_list = list_function.remove_value(profile_list, index)
        for person in profile_list:
            # remove all friends
            person.remove_friend(email)
        print("Successfully removed {} from profiles.".format(email))
    else:
        # not found
        print("{} is not found in profiles.".format(email))
    return profile_list

# Function show_proifile - show someone's profile
def show_profile(profile_list, person):
    output = "{} {} ({} | {})\n- {}\n".format(person.get_given_name(), person.get_family_name(), 
                person.get_gender(), person.get_email(), person.get_status())
    num = person.get_number_friends() 
    if num != 0:
        output += "- Friends (%s)\n" % num
        friends = person.get_friends_list()
        length = list_function.length(friends)
        for i in range(0, length):
            email = profile_list[find_profile(profile_list, friends[i])].get_email()
            if i != length - 1:
                output += "    " + email + "\n"
            else:
                output += "    " + email
    else:
        output += "- No friends yet..."
    print(output)

# Function update_profile() - update a profile
def update_profile(profile_list):
    email = input("\nPlease enter email address: ")
    index = find_profile(profile_list, email)
    person = profile_list[index]
    if index < 0:
        # not found
        print("{} is not found in profiles.\n".format(email))
    else:
        # found
        c = input("\nUpdate {} [status|add_friend|remove_friend]: ".format(get_friend_name(profile_list, email)))
        if c == "remove_friend":
            # remove friend
            f_email = input("\nPlease enter email address of friend to remove: ")
            if not person.is_friend(f_email):
                print("{} is not {}'s friend.\n".format(f_email, person.get_given_name()))
                return
            person.remove_friend(f_email)
            print("Removed {} updated profile is:\n".format(f_email))
            show_profile(profile_list, person)
        elif c == "add_friend":
            # add friend
            f_email = input("\nPlease enter email address of friend to add: ")
            f_index = find_profile(profile_list, f_email)
            if f_index == -1:
                print("{} is not found in profiles.\n".format(f_email))
                return
            if not person.add_friend(f_email):
                print("\n{} is already a friend.\n".format(get_friend_name(profile_list, f_email)))
                return
            show_profile(profile_list, profile_list[index])
        elif c == "status":
            # change status
            status = input("\nPlease enter status update: ")
            gname = person.get_given_name()
            fname = person.get_family_name()
            name = gname + " " + fname
            print("Updated status for {}: ".format(name))
            person.set_status(status)
            show_profile(profile_list, person)
        else:
            print("\nNot a valid command - returning to main menu.\n")

# Function get_friend_name()  get the friend's name
def get_friend_name(profile_list, email):
    for person in profile_list:
        if person.get_email() == email:
            name = person.get_given_name() + " " + person.get_family_name()
            return name

# Define a list to store Profile objects
profile_list = []


# Function main()  - main function
def main(profile_list):
    read_file("profiles.txt", profile_list)
    choice = input("Please enter choice [summary|add|remove|search|update|quit]: ")
    while choice != "quit":
        if choice == "add":
            add_profile(profile_list)
        elif choice == "summary":
            display_summary(profile_list)
        elif choice == "remove":
            profile_list = remove_profile(profile_list)
        elif choice == "search":
            email = input("\nPlease enter email address: ")
            index = find_profile(profile_list, email) 
            if index < 0:
                print("\n{} is not found in profiles.\n".format(email))
            else:
                print()
                person = profile_list[index]
                output = "{} {} ({} | {})\n- {}\n".format(person.get_given_name(), person.get_family_name(), 
                    person.get_gender(), person.get_email(), person.get_status())
                num = person.get_number_friends()
                if num == 0:
                    output += "- No friends yet..."
                else:
                    output += "- Friends (%s)\n" % num
                    friends = person.get_friends_list()
                    length = list_function.length(friends)
                    for i in range(0, length):
                        email = profile_list[find_profile(profile_list, friends[i])].get_email()
                        if i != length - 1:
                            output += "    " + email + "\n"
                        else:
                            output += "    " + email
                print(output)
        elif choice == "update":
            update_profile(profile_list)
        else:
            print("Not a valid command - please try again.")
        choice = input("Please enter choice [summary|add|remove|search|update|quit]: ")
    write_to_file("new_profiles.txt", profile_list)

main(profile_list)
# Terminating message
print("\n\n-- Program terminating --")
