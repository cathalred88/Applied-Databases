# main.py
# Author: Cathal Redmond
# Date: 2024-04-21
# Description: This is the main file for the Applied Databases project. It will contain the main code for the project.

# imports
import os
import pymysql


# connect to sql database
def connect_to_database():
    connection = pymysql.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )
    return connection



# write a main menu for the user to interact with a sql database
def main_menu():
    print("Conference Management")
    print("---------------------\n")
    print("MENU" )
    print("====")
    print("1 - View Speakers & Sessions")
    print("2 - View Attendees by Company")
    print("3 - Add New Attendee")
    print("4 - View Connected Attendees")
    print("5 - Add Attendee Connection")
    print("6 - View Rooms")
    print("X - Exit Application")

    choice = input("Choice: ")

    if choice == "1":
        ViewSpeakersAndSessions()
    elif choice == "2":
        ViewAttendeesByCompany()
    elif choice == "3":
        AddNewAttendee()
    elif choice == "4":
        ViewConnectedAttendees()
    elif choice == "5":
        AddAttendeeConnection()
    elif choice == "6":
        ViewRooms()
    elif choice == "X" or choice == "x":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

# functions for each menu option
def ViewSpeakersAndSessions():
    print("View Speakers & Sessions")
    # code to view speakers and sessions from stored database
    speaker = input("Enter speaker name: ")
    # ... (code to fetch and display speaker information)

    # clear the terminal window after displaying the information
    os.system("cls" if os.name == "nt" else "clear")

    # return to main menu
    main_menu()

def ViewAttendeesByCompany():
    print("View Attendees by Company")
    # code to view attendees by company
    company = input("Enter company name: ")
    # ... (code to fetch and display attendees for the specified company)

    # clear the terminal window after displaying the information
    os.system("cls" if os.name == "nt" else "clear")

    # return to main menu
    main_menu()

def AddNewAttendee():
    print("Add New Attendee")
    # code to add new attendee

    # return to main menu
    main_menu()

def ViewConnectedAttendees():
    print("View Connected Attendees")
    # code to view connected attendees

    # return to main menu
    main_menu()

def AddAttendeeConnection():
    print("Add Attendee Connection")
    # code to add attendee connection

    # return to main menu
    main_menu() 

def ViewRooms():
    print("View Rooms")
    # code to view rooms

    # return to main menu
    main_menu()


# call the main menu function
if __name__ == "__main__":
    main_menu()

# End of main.py code