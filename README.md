# 📅 Event Management System (EMS)

> **A robust console-based application designed to manage events, bookings, and reporting using core Python concepts.**

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

## 📖 Overview

This project was developed as part of the **L&T Python Refresher Program**. It serves as a practical demonstration of distinct data management (venues, dates, pricing, attendee counts) without relying on external databases.

The system replaces manual record-keeping by utilizing **File Handling** for data persistence and generating a dynamic **HTML Dashboard** for visual reporting.

## 🚀 Key Features

- **Add Events**: Create new events with validation for name, date, and pricing.
- **Book Tickets**: Real-time booking system that updates attendee counts instantly.
- **Data Persistence**: All data is saved to `events_data.txt` (CSV format), ensuring nothing is lost when the program closes.
- **Auto-Generated Reports**: Generates a styled `dashboard.html` file and automatically opens it in your browser.
- **Error Handling**: Robust inputs (e.g., preventing text in price fields) to ensure the application never crashes.

## 🛠️ Technical Showcase

This project is architected to demonstrate mastery of the following Python concepts:

- **OOP (Object Oriented Programming)**:
  - `Event` Class: Blueprint for data objects.
  - `EventManager` Class: Encapsulates business logic and file operations.
- **Modular Programming**: Code is split into logical modules (`main.py`, `manager.py`, `event.py`) for better maintainability.
- **File Handling**: Manual parsing of CSV data and programmatic generation of HTML files.

## 📂 Project Structure

````bash
Event-Management-System/
│
├── assets/                  # 📸 Screenshots for documentation
│   ├── add_event.png
│   ├── booking.png
│   ├── menu.png
│   └── report.png
│
├── reports/                 # 📊 Visual Output
│   └── dashboard.html       # (Auto-generated HTML Report)
│
├── event.py                 # 🐍 Module: Event Object Blueprint
├── events_data.txt          # 💾 Database (CSV format)
├── manager.py               # 🐍 Module: Logic & File Handling
├── main.py                  # 🐍 Entry Point (Run this file)
│
└── README.md                # 📄 Project Documentation


## 🧰 Installation & Run

Since this project uses Python's Standard Library, no external installation (`pip install`) is required.

### 1. **Clone the repository**
```bash
git clone https://github.com/mahii-17/Event-management-System.git
cd Event-management-System
```

### 2. **Run the application**
```bash
python main.py
```


## 📸 Application Walkthrough

### 1. 🏠 Main Menu
The application launches a clean CLI loop that remains active until `Exit` is selected.
Navigate using **number key options**.

### 2. ✨ Adding an Event
Users can input event details. The system validates:
- **Price** ➝ must be numeric
- **Date** ➝ stored in correct format

🗂 **Backend Storage:** Data is instantly saved in
`events_data.txt`

🖼 Icon: `assets/add_event.png`

### 3. 🎟 Booking Tickets
Reads the database in real time, displays all listed events, and lets the user increase attendee counts.

🛡 **Validation:** Prevents invalid event IDs to avoid crashes.

🖼 Icon: `assets/booking.png`

### 4. 📊 Visual Reporting
Processes text data and generates a **styled HTML report** in:
- `reports/dashboard.html`

Then automatically opens in the default browser.

🖼 Icon: `assets/report.png`

---

## 🔮 Future Scope

| Feature | Description |
|---------|------------|
| 💻 GUI Version | Port logic to Tkinter / PyQt for desktop UI |
| ✉ Email Integration | Auto email confirmation after booking |
| 🗄 Database Migration | Move from `.txt` to SQLite for scalable queries |

---

### 🏗 Built With
- Python 🐍
- CLI-based interface
- Custom HTML rendering

© 2025 | Event Management System
````
