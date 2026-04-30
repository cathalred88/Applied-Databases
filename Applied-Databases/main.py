# main.py
# Author: Cathal Redmond
# Date: 2024-04-21
# Description: This is the main file for the Applied Databases project. It will contain the main code for the project.

# imports
import os
import pymysql
from tabulate import tabulate

conn = None
driver = None

# connect to sql database
def connect_to_database():
    global conn
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="appdbproj",
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Connected to database successfully!")
    except Exception as e:
        print(f"Error connecting to database: {e}")


print("this is working")


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
    print("View Speakers & Sessions\n")
    speaker = input("Enter speaker name:")

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM session WHERE speakerName LIKE %s",
                (f"%{speaker}%",)
            )
            result = cursor.fetchall()

            if result:
                print(f"Session Details for {speaker}:")
                table_data = [
                    [row["speakerName"], row["sessionTitle"], row["roomID"]]
                    for row in result
                ]
                headers = ["Speaker Name", "Session Title", "Room ID"]
                print(tabulate(table_data, headers=headers, tablefmt="grid"))
            else:
                # if not speaker is found to match the search query, offer to search for another name
                search_again = input("Speaker not found. Search again? (y/n): ")
                if search_again.lower() == "y":
                    ViewSpeakersAndSessions()
                else:
                    print("Speaker not found.")
    except Exception as e:
        print(f"Error fetching speaker: {e}")

    main_menu()

def ViewAttendeesByCompany():
    print("View Attendees by Company")
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
    connect_to_database()
    if conn:
        main_menu()
else:
    pass

# End of main.py code