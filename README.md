# 📚 Advanced Attendance Management System (Python + Tkinter + SQLite)

This project is a robust **Attendance Management System** built using **Python**, **Tkinter** for the GUI, and **SQLite** for persistent storage. It allows teachers or administrators to maintain daily attendance records, store them in a database, and view saved entries — all with a simple graphical interface.

---

## 📑 Table of Contents

- [📌 Features](#-features)
- [💻 Tech Stack](#-tech-stack)
- [🔧 How It Works](#-how-it-works)
- [🚀 Getting Started](#-getting-started)
- [🗂 Project Structure](#-project-structure)
---

## 📌 Features

✅ Persistent student list stored in SQLite  
✅ Add new students dynamically  
✅ Mark attendance with dropdowns for Present/Absent  
✅ Save daily attendance into database  
✅ View saved attendance records for a selected date  
✅ Easy-to-use and interactive GUI  
✅ Fully offline and portable (no internet required)  

---

## 💻 Tech Stack

| Component     | Description                                |
|---------------|--------------------------------------------|
| Python        | Programming language                       |
| Tkinter       | GUI toolkit for building the interface     |
| SQLite        | Embedded database engine                   |
| `datetime`    | Timestamp and date handling                |

All technologies used are part of the **Python Standard Library**, so no external installation is required!

---

## 🔧 How It Works

1. **Startup**  
   - Connects to `attendance.db` or creates it if not found.
   - Loads all registered student names from the database.

2. **Marking Attendance**  
   - For each student, select "Present" or "Absent" from the dropdown.
   - Attendance is stored against the selected date.

3. **Adding Students**  
   - Enter a new student's name.
   - If the name doesn't already exist, it is added to the database and the list refreshes.

4. **Viewing Attendance Records**  
   - You can load records for a specific date from the database into a table.

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.x installed on your system

### 📦 Run the Application

---

## 🗂 Project Structure

- Enchanced_attendance_management/
- ├── attendance_sqlite.py      # Main application script
- ├── attendance.db             # SQLite database (created automatically)
- ├── README.md                 # Documentation
