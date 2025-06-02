import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

# --- Database Setup ---
conn = sqlite3.connect('attendance.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT UNIQUE)''')
c.execute('''CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY,
    student_name TEXT,
    status TEXT,
    date TEXT
)''')
conn.commit()

def get_students():
    c.execute("SELECT name FROM students")
    return [row[0] for row in c.fetchall()]

def add_student_to_db(name):
    try:
        c.execute("INSERT INTO students (name) VALUES (?)", (name,))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def save_attendance(date, attendance_dict):
    for name, status in attendance_dict.items():
        c.execute("INSERT INTO attendance (student_name, status, date) VALUES (?, ?, ?)", (name, status, date))
    conn.commit()

def fetch_attendance_records(date):
    c.execute("SELECT student_name, status FROM attendance WHERE date = ?", (date,))
    return c.fetchall()

# --- GUI Setup ---
root = tk.Tk()
root.title("Advanced Attendance System")
root.geometry("600x600")

# --- UI Variables ---
attendance_vars = {}
selected_date = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))

# --- Functions ---

def refresh_students():
    for widget in student_frame.winfo_children():
        widget.destroy()
    attendance_vars.clear()

    students = get_students()
    for i, name in enumerate(students):
        tk.Label(student_frame, text=name, width=20).grid(row=i, column=0, pady=2, padx=5)
        var = tk.StringVar(value="None")
        attendance_vars[name] = var
        ttk.Combobox(student_frame, textvariable=var, values=["Present", "Absent"], width=10, state="readonly").grid(row=i, column=1)

def submit_attendance():
    date = selected_date.get()
    if not date:
        messagebox.showerror("Date Missing", "Please enter a date.")
        return

    data = {name: var.get() for name, var in attendance_vars.items() if var.get() != "None"}

    if not data:
        messagebox.showwarning("No Data", "No attendance marked.")
        return

    save_attendance(date, data)
    messagebox.showinfo("Success", f"Attendance for {date} saved.")
    load_attendance_records()

def add_student():
    name = new_student_entry.get().strip()
    if name:
        if add_student_to_db(name):
            new_student_entry.delete(0, tk.END)
            refresh_students()
        else:
            messagebox.showwarning("Duplicate", f"{name} already exists.")

def load_attendance_records():
    for row in tree.get_children():
        tree.delete(row)
    date = selected_date.get()
    records = fetch_attendance_records(date)
    for name, status in records:
        tree.insert('', tk.END, values=(name, status, date))

# --- UI Layout ---

tk.Label(root, text="Attendance Management System", font=("Arial", 16, "bold")).pack(pady=10)

# Date Input
date_frame = tk.Frame(root)
date_frame.pack(pady=5)
tk.Label(date_frame, text="Date (YYYY-MM-DD):").pack(side=tk.LEFT)
tk.Entry(date_frame, textvariable=selected_date, width=15).pack(side=tk.LEFT)

# Student Frame
student_frame = tk.Frame(root)
student_frame.pack(pady=10)

refresh_students()

# Add Student
tk.Label(root, text="Add New Student:").pack()
new_student_entry = tk.Entry(root)
new_student_entry.pack()
tk.Button(root, text="Add Student", command=add_student, bg="#4CAF50", fg="white").pack(pady=5)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Submit Attendance", command=submit_attendance, bg="#2196F3", fg="white", width=18).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Load Attendance Records", command=load_attendance_records, bg="#FFC107", width=22).pack(side=tk.LEFT, padx=5)

# Attendance Table
tree = ttk.Treeview(root, columns=("Name", "Status", "Date"), show='headings')
tree.heading("Name", text="Student Name")
tree.heading("Status", text="Status")
tree.heading("Date", text="Date")
tree.pack(expand=True, fill="both", pady=10)

tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()
