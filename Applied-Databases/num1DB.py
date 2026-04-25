# num1DB.py 
# This file contains the code for the conference management system that interacts with a SQL database. 
# It includes functions for viewing speakers and sessions, viewing attendees by company, adding new attendees, viewing connected attendees, adding attendee connections, and viewing rooms. 
# The main menu allows users to select these options and interact with the database accordingly.

import pymysql
import neo4j


conn = None
driver = None

def connect_to_database():
    global conn
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="appdbproj`"
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Connected to database successfully!")
    except Exception as e:
        print(f"Error connecting to database: {e}")

def get_speakers_and_sessions():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM speakers")
        speakers = cursor.fetchall()
        for speaker in speakers:
            print(f"Speaker: {speaker['name']}, Session: {speaker['session']}")

def get_attendees_by_company(company_name):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM attendees WHERE company = %s", (company_name,))
        attendees = cursor.fetchall()
        for attendee in attendees:
            print(f"Attendee: {attendee['name']}, Company: {attendee['company']}")

def add_new_attendee(name, company):
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO attendees (name, company) VALUES (%s, %s)", (name, company))
        conn.commit()
        print("New attendee added successfully!")   

def get_connected_attendees():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM connections")
        connections = cursor.fetchall()
        for connection in connections:
            print(f"Attendee 1: {connection['attendee1']}, Attendee 2: {connection['attendee2']}")  

def add_attendee_connection(attendee1, attendee2):
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO connections (attendee1, attendee2) VALUES (%s, %s)", (attendee1, attendee2))
        conn.commit()
        print("Attendee connection added successfully!")

def get_rooms():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM rooms")
        rooms = cursor.fetchall()
        for room in rooms:
            print(f"Room: {room['name']}, Capacity: {room['capacity']}")

if __name__ == "__main__":
    connect_to_database()
    # Example usage:
    get_speakers_and_sessions()
    get_attendees_by_company("Tech Company")
    add_new_attendee("John Doe", "Tech Company")
    get_connected_attendees()
    add_attendee_connection("John Doe", "Jane Smith")
    get_rooms()

# Note: The above code assumes that the database schema includes tables for speakers, attendees, connections, and rooms with the appropriate columns. 
# Adjust the SQL queries as needed based on your actual database schema.

