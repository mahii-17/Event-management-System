Event Management System (EMS) 📅

1. General Introduction

Events involve managing distinct data points: venues, dates, pricing, and attendee counts. This Event Management System (EMS) is a robust console-based application designed to replace manual record-keeping.

It utilizes File Handling to ensure data persists even after the program closes, and creates a dynamic HTML Dashboard for visual reporting.

2. Technical Showcase

This project was architected specifically to demonstrate mastery of the core Python concepts covered in the refresher program:

OOP (Object Oriented Programming):

Event Class: Acts as a blueprint for data objects.

EventManager Class: Encapsulates business logic and file operations.

File Handling:

Read/Write: Manually parses CSV data from events_data.txt.

Report Generation: Programmatically creates an external dashboard.html file using string manipulation.

Exception Handling:

Robust try-except blocks prevent crashes during invalid user input (e.g., entering text for price).

Safely handles missing directories or files using os.path.

Modular Programming:

Code is split into logical modules (main.py, manager.py, event.py) rather than one large script.

3. Project Structure

Event-Management-System/
│
├── assets/ # 📸 Screenshots for documentation
│ ├── menu.png
│ ├── add_event.png
│ ├── booking.png
│ └── report.png
│
├── data/ # 💾 Database storage
│ └── events_data.txt # (Auto-generated CSV file)
│
├── reports/ # 📊 Visual Output
│ └── dashboard.html # (Auto-generated HTML Report)
│
├── event.py # 🐍 Module: Event Object Blueprint
├── manager.py # 🐍 Module: Logic & File Handling
├── main.py # 🐍 Entry Point (Run this file)
│
└── README.md # 📄 Project Documentation

4. How to Run

Since this project uses Python's Standard Library, no external installation (pip install) is required.

Clone the repository:

git clone [https://github.com/your-username/Event-Management-System.git](https://github.com/your-username/Event-Management-System.git)
cd Event-Management-System

Run the application:

python main.py

5. Application Walkthrough

1. Main Menu

The application launches a CLI (Command Line Interface) loop that stays active until the user chooses to exit.

2. Adding an Event (Data Entry)

Users can input event details. This module uses Exception Handling to ensure Price is always a valid number.

Input: Name, Date, Price.

Backend: Data is immediately committed to data/events_data.txt.

3. Booking Tickets

This module reads the database in real-time. It lists all active events and allows the user to increment the attendee count.

Validation: If a user selects an invalid ID (e.g., "3" when only 1 event exists), the system catches the error and prompts again to ensure stability.

4. HTML Report Generation

The standout feature. By processing the text data, the Python script generates a styled HTML table and automatically launches your default web browser to display it.

6. Future Scope

GUI Version: Porting the logic to Tkinter for a desktop window experience.

Email Integration: Sending automatic confirmation emails to attendees.

Database Migration: Upgrading from Text Files to SQLite for complex queries.

© 2025 | Built with Python 🐍
This is a mini project for L&T Python Refresher Program.
