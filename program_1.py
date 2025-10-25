# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names, 
# and displays their first, middle, and last initials.  
# For example, if the user enters John William Smith, the program should display J. W. S.

# Title: Initials
# Author: Arianna Endres
# Date: 10/24/2025

def initials_generator(personsName):

    personsInitials = ""
    name = personsName.split()

    for word in name:
        print(word[0].upper() + '. ', end = '')

    return personsInitials.strip()

personsName = input('Enter the users first, middle, and last name: ')

initials = initials_generator(personsName)

print(initials)