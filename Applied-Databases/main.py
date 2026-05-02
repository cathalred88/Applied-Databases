# main.py
# Author: Cathal Redmond
# Date: 2024-04-21
# Description: This is the main file for the Applied Databases project. It will contain the main code for the project.

# imports
import os
from altair import URI
from hyperlink import URL
import pymysql
from tabulate import tabulate
from datetime import datetime
from neo4j import GraphDatabase


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


# main menu for the user to select menu options
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
        print("\n")
        print("Thank you for using the Conference Management System, Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

## Modules for each menu option

# Module 1: View Speakers and Sessions:
def ViewSpeakersAndSessions():
    print("View Speakers & Sessions\n")

    while True:
        speaker = input("Enter speaker name queary: ")

        try:
            with conn.cursor() as cursor:

                query = """
                SELECT 
                    s.speakerName,
                    s.sessionTitle,
                    r.roomName
                FROM session s
                JOIN room r ON s.roomID = r.roomID
                WHERE s.speakerName LIKE %s;
                """

                cursor.execute(query, (f"%{speaker}%",))
                result = cursor.fetchall()

                if result:
                    print(f"\nSession Details for all speakers with names containing '{speaker}':")
                    print("\n")

                    table_data = [
                        [
                            row["speakerName"],
                            row["sessionTitle"],
                            row["roomName"]
                        ]
                        for row in result
                    ]

                    headers = ["Speaker Name", "Session Title", "Room"]
                    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
                    print("\n")

                    break  # Exit loop after success

                else:
                    search_again = input("No Speakers found of that name. Search again? (y/n): ")
                    if search_again.lower() != "y":
                        print("Returning to menu...\n")
                        break

        except Exception as e:
            print(f"Error fetching speaker: {e}")
            break

# return to main menu after completing
    main_menu()


# Module 2: View Attendees by Company:
def ViewAttendeesByCompany():
    print("View Attendees by Company\n")

    while True:  # loop until valid or user exits
        company = input("Enter company ID: ")

        try:
            with conn.cursor() as cursor:

                # Step 1 — Check if company exists
                cursor.execute(
                    "SELECT companyName, companyID FROM company WHERE companyID = %s",
                    ({company},)
                )
                company_result = cursor.fetchall()

                if not company_result:
                    retry = input("Company not found. Try again? (y/n): ")
                    if retry.lower() == "y":
                        continue
                    else:
                        print("Returning to menu...\n")
                        break

                company_id = company_result[0]["companyID"]
                company_name = company_result[0]["companyName"]

                # Step 2 — Fetch registrations
                query = """
                SELECT 
                    a.attendeeName,
                    a.attendeeDOB,
                    s.sessionTitle,
                    s.speakerName,
                    s.sessionDate,
                    r.roomName
                FROM attendee a
                JOIN registration reg ON a.attendeeID = reg.attendeeID
                JOIN session s ON reg.sessionID = s.sessionID
                JOIN room r ON s.roomID = r.roomID
                WHERE a.attendeeCompanyID = %s;
                """

                cursor.execute(query, (company_id,))
                result = cursor.fetchall()

                print(f"\nCompany: {company_name}\n")

                if result:
                    table_data = [
                        [
                            row["attendeeName"],
                            row["attendeeDOB"],
                            row["sessionTitle"],
                            row["speakerName"],
                            row["sessionDate"],
                            row["roomName"]
                        ]
                        for row in result
                    ]

                    headers = [
                        "Attendee Name",
                        "DOB",
                        "Session Title",
                        "Speaker",
                        "Session Date",
                        "Room"
                    ]

                    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
                    print("\n")

                else:
                    print("This company has no attendees registered for sessions.\n")

                break  # Exit loop after successful lookup

        except Exception as e:
            print(f"Error fetching Company data: {e}")
            print("\n")
            break
    
    # return to main menu
    main_menu()


# Module 3: Add New Attendee
def AddNewAttendee():

    print("Add New Attendee\n")

    # Validate Attendee ID
    while True:
        attendee_ID = input("Enter attendee ID: ").strip()

        if not attendee_ID.isdigit():
            print("Error: Attendee ID must be a number.\n")
            continue

        attendee_ID = int(attendee_ID)

        # Check for duplicates in database
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT attendeeID FROM attendee WHERE attendeeID = %s",
                (attendee_ID,)
            )
        if cursor.fetchone():
            print("Error: Attendee ID already exists. Please enter a different ID.\n")
            continue

        break

    # Validate Name
    while True:
        attendee_name = input("Enter attendee name: ").strip()
        if attendee_name == "":
            print("Error: Attendee name cannot be blank.\n")
        else:
            break

    # Validate DOB
    while True:
        attendee_dob = input("Enter attendee date of birth (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(attendee_dob, "%Y-%m-%d")
            break
        except ValueError:
            print("Error: Date must be in format YYYY-MM-DD.\n")

    # Validate Gender
    while True:
        attendee_gender = input("Enter attendee gender (Male/Female): ").strip().capitalize()
        if attendee_gender in ["Male", "Female"]:
            break
        else:
            print("Error: Gender must be 'Male' or 'Female'.\n")

    # Validate Company ID
    while True:
        attendee_company_id = input("Enter attendee company ID: ").strip()
        if attendee_company_id.isdigit():
            attendee_company_id = int(attendee_company_id)
            break
        else:
            print("Error: Company ID must be a number.\n")

    try:
        with conn.cursor() as cursor:

            # Check Company Exists
            cursor.execute(
                "SELECT companyName FROM company WHERE companyID = %s",
                (attendee_company_id,)
            )
            company_result = cursor.fetchone()

            if not company_result:
                print("Error: Company ID does not exist.\n")
                return

            # Insert Attendee
            cursor.execute(
                """
                INSERT INTO attendee
                (attendeeID, attendeeName, attendeeDOB, attendeeGender, attendeeCompanyID)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (attendee_ID, attendee_name, attendee_dob, attendee_gender, attendee_company_id)
            )

            print("\nAttendee added successfully!")

            # Show Available Sessions
            cursor.execute("SELECT sessionID, sessionTitle FROM session")
            sessions = cursor.fetchall()

            print("\nAvailable Sessions:")
            for row in sessions:
                print(f"{row['sessionID']} - {row['sessionTitle']}")

            # Register for Session
            while True:
                session_id = input("\nEnter Session ID to register attendee: ").strip()
                if session_id.isdigit():
                    session_id = int(session_id)
                    break
                else:
                    print("Error: Session ID must be a number.\n")

            # Generate Next Registration ID
            cursor.execute("SELECT MAX(registrationID) FROM registration")
            max_id = cursor.fetchone()["MAX(registrationID)"]

            if max_id is None:
                new_registration_id = 1
            else:
                new_registration_id = max_id + 1

            # Insert Registration into database
            cursor.execute(
                """
                INSERT INTO registration
                (registrationID, attendeeID, sessionID, registeredAt)
                VALUES (%s, %s, %s, NOW())
                """,
                (new_registration_id, attendee_ID, session_id)
            )

            conn.commit()
            print("Attendee successfully registered for session!\n")

    except Exception as e:
        print(f"Error: {e}")

    # return to main menu
    main_menu()




# Module 4: View Connected Attendees
def ViewConnectedAttendees():
    print("View Connected Attendees")
    # code to view connected attendees from the neo4j database

    URI = "bolt://localhost:7687"
    USERNAME = "neo4j"
    PASSWORD = "neo4jneo4j"

    driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

    with driver.session() as session:
        result = session.run("RETURN 'Connected to Aura!' AS msg")
        print(result.single()["msg"])

        # enter attendee ID to search for the neo4j database connections 
        attendee_id = input("Enter Attendee ID: ").strip()
        

    driver.close()

    # return to main menu
    main_menu()


# Module 5: Add Attendee Connection
def AddAttendeeConnection():
    print("Add Attendee Connection")
    # code to add attendee connection

    # return to main menu
    main_menu() 


# Module 6: View Rooms
def ViewRooms():
    print("View Rooms")
    # code to view rooms

    # return to main menu
    main_menu()

## Main Program 
# call the main menu function
if __name__ == "__main__":
    connect_to_database()
    if conn:
        main_menu()
else:
    pass

# End of main.py code