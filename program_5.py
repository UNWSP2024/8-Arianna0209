# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

# Title: Course Catalogue
# Author: Arianna Endres
# Date: 10/24/2025

def input_courses():
    course_catalogue = {}

    add_more_courses = 'y'

    while add_more_courses == 'y':
        course_ID = input("Enter the course ID: ").upper()
        course_name = input("Enter the corresponding course name: ")

        course_catalogue[course_ID] = course_name

        add_more_courses = input('Would you like to add more courses? (Y/N) ').lower()

    return course_catalogue

def check_for_courses(course_catalogue):

    search_for_courses = 'y'

    while search_for_courses == 'y':
        subject = input('Enter the three letter code for the subject '
                        'you would like to search for: ').upper()

        matching_courses = {}

        for key in course_catalogue:
            if key[:3] == subject:
                matching_courses[key] = course_catalogue[key]

        print(f'The following courses are available for the {subject} subject: {matching_courses}.')

        search_for_courses = input('Would you like to search for more courses? (Y/N) ').lower()

def main():
    course_catalogue = input_courses()
    check_for_courses(course_catalogue)

main()
