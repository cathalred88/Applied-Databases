📊 Applied Databases – Conference Management System

A Python-based Conference Management System developed for the Applied Databases module.
The system demonstrates integration between MySQL (relational database) and Neo4j (graph database) to manage conference attendees, sessions, rooms, and attendee relationships.

📖 Overview

This project is a console-based application that allows users to manage a conference environment. It supports attendee registration, session management, room occupancy tracking, and social connections between attendees.

It demonstrates:

Relational database querying with MySQL
Graph relationships using Neo4j
Hybrid database integration in a single application
Real-world CRUD operations
Aggregation queries and reporting
🧱 Technologies Used
🐍 Python 3
🐬 MySQL (PyMySQL connector)
🧠 Neo4j Graph Database
📊 Tabulate (for formatted console output)
⏱ Datetime (for timestamps)
🗂 Project Structure
main.py              # Main application (menu + all modules)
num1DB.py            # Supporting database logic / utilities
test.py              # Testing script
this_testfile.py     # Additional test file
sandbox.ipynb        # Experimentation notebook
requirements.txt     # Python dependencies
⚙️ Database Setup
MySQL Database

The system connects to a local MySQL database:

Database name: appdbproj
Host: localhost
User: root
Password: root

Main tables used:

attendee
company
session
room
registration
Neo4j Database

Used for modelling attendee relationships.

URI: bolt://localhost:7687

Default credentials used in code:

username: neo4j
password: neo4jneo4j

Relationship type:

(:Attendee)-[:CONNECTED_TO]->(:Attendee)
🚀 How to Run the Project
1. Install dependencies
pip install pymysql tabulate neo4j
2. Start MySQL and Neo4j

Ensure both databases are running locally before launching the application.

3. Run the application
python main.py
🧭 Application Menu

When launched, the system provides a console menu:

1 - View Speakers & Sessions
2 - View Attendees by Company
3 - Add New Attendee
4 - View Connected Attendees
5 - Add Attendee Connection
6 - View Rooms
X - Exit Application
📌 Key Features
🎤 1. View Speakers & Sessions
Search speakers by name (partial match)
Displays session title and room allocation
🏢 2. View Attendees by Company
Displays attendees linked to a selected company
Shows session registrations and room details
➕ 3. Add New Attendee
Input validation for:
ID uniqueness
Date of birth format
Gender selection
Company validation
Automatically registers attendee into a session
🌐 4. View Connected Attendees (Neo4j)
Displays social connections between attendees
Uses graph relationships (CONNECTED_TO)
🔗 5. Add Attendee Connection (Neo4j)
Creates a bidirectional relationship between two attendees
Prevents duplicate connections
🏫 6. View Rooms & Occupancy
Displays room capacity
Session scheduling
Calculates occupancy percentage per session
🧠 Database Design Concepts Demonstrated
Relational schema design (MySQL)
JOIN operations across multiple tables
Aggregation queries (COUNT, GROUP BY)
Graph relationships (Neo4j)
Data validation & integrity checks
Hybrid database architecture
📊 Example Query Features
Filter speakers using LIKE queries
Compute room occupancy percentage:
COUNT(reg.registrationID) / r.capacity * 100
Retrieve graph connections using Cypher:
MATCH (a:Attendee)-[:CONNECTED_TO]->(b:Attendee)
⚠️ Notes
Ensure MySQL credentials match your local setup
Neo4j must be running before using connection features
Both databases must contain preloaded schema/data for full functionality
Console-based interface (no web frontend)
👤 Author

Cathal Redmond
Applied Databases Coursework Project

📄 License

Academic use only – not intended for production deployment.
