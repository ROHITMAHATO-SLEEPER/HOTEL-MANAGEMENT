import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database Setup
conn = sqlite3.connect("railway_reservation.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        train TEXT,
        source TEXT,
        destination TEXT
    )
''')
conn.commit()

# Booking Function
def book_ticket():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    train = entry_train.get()
    source = entry_source.get()
    destination = entry_destination.get()

    if name and age and gender and train and source and destination:
        cursor.execute("INSERT INTO reservations (name, age, gender, train, source, destination) VALUES (?, ?, ?, ?, ?, ?)",
                       (name, age, gender, train, source, destination))
        conn.commit()
        messagebox.showinfo("Success", "Ticket booked successfully!")
        clear_fields()
    else:
        messagebox.showwarning("Missing Info", "Please fill all fields!")

# View Bookings Function
def view_bookings():
    cursor.execute("SELECT * FROM reservations")
    records = cursor.fetchall()
    view_window = tk.Toplevel(root)
    view_window.title("All Bookings")
    for index, record in enumerate(records):
        tk.Label(view_window, text=str(record)).grid(row=index, column=0, sticky='w')

# Cancel Booking
def cancel_booking():
    booking_id = entry_cancel_id.get()
    if booking_id:
        cursor.execute("DELETE FROM reservations WHERE id = ?", (booking_id,))
        conn.commit()
        if cursor.rowcount:
            messagebox.showinfo("Cancelled", "Booking cancelled.")
        else:
            messagebox.showerror("Error", "No such booking ID found.")
    else:
        messagebox.showwarning("Input Required", "Enter booking ID to cancel.")

# Clear all fields
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_train.delete(0, tk.END)
    entry_source.delete(0, tk.END)
    entry_destination.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Railway Reservation System")
root.geometry("400x500")

tk.Label(root, text="Passenger Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Age:").pack()
entry_age = tk.Entry(root)
entry_age.pack()

tk.Label(root, text="Gender:").pack()
gender_var = tk.StringVar()
tk.OptionMenu(root, gender_var, "Male", "Female", "Other").pack()

tk.Label(root, text="Train Name/Number:").pack()
entry_train = tk.Entry(root)
entry_train.pack()

tk.Label(root, text="Source Station:").pack()
entry_source = tk.Entry(root)
entry_source.pack()

tk.Label(root, text="Destination Station:").pack()
entry_destination = tk.Entry(root)
entry_destination.pack()

tk.Button(root, text="Book Ticket", command=book_ticket, bg="green", fg="white").pack(pady=10)
tk.Button(root, text="View All Bookings", command=view_bookings).pack(pady=5)

tk.Label(root, text="Cancel Booking (Enter Booking ID):").pack()
entry_cancel_id = tk.Entry(root)
entry_cancel_id.pack()
tk.Button(root, text="Cancel Booking", command=cancel_booking, bg="red", fg="white").pack(pady=10)

root.mainloop()