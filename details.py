from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import random
from time import strftime
from datetime import datetime
class dtroom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # Title
        self.var_floor = StringVar()
        self.var_roomno = StringVar()
        self.var_roomtype = StringVar()
         # ========== Title ==========
        lbl_title = Label(self.root, text="ROOM AVAILABLE DETAILS", font=("times new roman", 18, "bold"), bg="green", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        img2 = Image.open("C:/Users/Rohit mahato/HMS IMAGE/logo.png")
        img2 = img2.resize((100, 40))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=6, y=2, width=100, height=40)

         # ========== Room Details Frame ==========
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="ROOM DETAILS", padx=2, font=("times new roman", 12, "bold"))
        labelframeleft.place(x=5, y=50, width=540, height=350)

           # ========== FLOOR ==========
        Label(labelframeleft, text="FLOOR:", font=("arial", 12, "bold")).grid(row=0, column=0, sticky=W, padx=2, pady=6)
        ttk.Entry(labelframeleft, textvariable=self.var_floor, width=20, font=("arial", 13, "bold")).grid(row=0, column=1, sticky=W)

        # ========== ROOM NO ==========
        Label(labelframeleft, text="ROOM NO:", font=("arial", 12, "bold")).grid(row=1, column=0, sticky=W, padx=2, pady=6)
        ttk.Entry(labelframeleft, textvariable=self.var_roomno, width=20, font=("arial", 13, "bold")).grid(row=1, column=1, sticky=W)


        # ========== ROOM TYPE ==========
        Label(labelframeleft, text="ROOM TYPE:", font=("arial", 12, "bold")).grid(row=2, column=0, sticky=W, padx=2, pady=6)
        ttk.Combobox(labelframeleft, textvariable=self.var_roomtype, width=18, font=("arial", 13, "bold"), state='readonly', values=["Single", "Double", "Luxury"]).grid(row=2, column=1, sticky=W)

        btnframe = Frame(labelframeleft, bd=2, relief=RIDGE)
        btnframe.place(x=0, y=200, width=412, height=40)

        Button(btnframe, text="ADD",command=self.add_data , font=("arial", 12, "bold"), bg="black", fg="gold", width=9).grid(row=0, column=0, padx=1)
        Button(btnframe, text="UPDATE" ,command=self.update,font=("arial", 12, "bold"), bg="black", fg="gold", width=9).grid(row=0, column=1, padx=1)
        Button(btnframe, text="DELETE",command=self.deletefn,font=("arial", 12, "bold"), bg="black", fg="gold", width=9).grid(row=0, column=2, padx=1)
        Button(btnframe, text="RESET",command=self.reset_data,font=("arial", 12, "bold"), bg="black", fg="gold", width=9).grid(row=0, column=3, padx=1)

        # ========== Search and Table ==========
        tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="SHOW AVAILABLE ROOM", padx=2, font=("times new roman", 12, "bold"))
        tableframe.place(x=600, y=55, width=600, height=350)

        scrollx = ttk.Scrollbar(tableframe, orient=HORIZONTAL)
        scrolly = ttk.Scrollbar(tableframe, orient=VERTICAL)

        self.roomtable = ttk.Treeview(tableframe,
                                      columns=("FLOOR","ROOMNO", "ROOMTYPE"),
                                      xscrollcommand=scrollx.set,
                                      yscrollcommand=scrolly.set)
                                      

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.roomtable.xview)
        scrolly.config(command=self.roomtable.yview)

        self.roomtable.heading("FLOOR", text="FLOOR")
        self.roomtable.heading("ROOMNO", text="ROOMNO")
        self.roomtable.heading("ROOMTYPE", text="ROOMTYPE")
        for col in self.roomtable["columns"]:
            self.roomtable.heading(col, text=col)
            self.roomtable.column(col, width=100)

        self.roomtable["show"] = "headings"
        self.roomtable.pack(fill=BOTH, expand=1)   
        self.roomtable.bind("<ButtonRelease-1>", self.getcursor)
        self.fetch_data()

    # ===================add new data to  the system===================
    def add_data(self):
        if self.var_roomno.get() == "" or self.var_floor.get() == "" or self.var_roomtype.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="ROHIT@123", database="hotel11")
                mycursor = conn.cursor()
                mycursor.execute("INSERT INTO roomdetails VALUES (%s,%s,%s)", (
                   self.var_floor.get(),
                   self.var_roomno.get(),
                   self.var_roomtype.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "New room added successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)    

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="ROHIT@123", database="hotel11")
            mycursor = conn.cursor()
            mycursor.execute("SELECT * FROM roomdetails")
            rows = mycursor.fetchall()
            if rows:
                self.roomtable.delete(*self.roomtable.get_children())
                for row in rows:
                    self.roomtable.insert("", END, values=row)
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error fetching data: {str(es)}", parent=self.root)

    def getcursor(self, event=""):
        cursor_row = self.roomtable.focus()
        content = self.roomtable.item(cursor_row)
        row = content["values"]
        self.var_floor.set(row[0])
        self.var_roomno.set(row[1])
        self.var_roomtype.set(row[2])

    def update(self):
        if self.var_floor.get() == "" or self.var_roomno.get() == "" or self.var_roomtype.get() == "":
            messagebox.showerror("Error", "Please enter all fields", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="ROHIT@123", database="hotel11")
            mycursor = conn.cursor()
            mycursor.execute(
                "UPDATE roomdetails SET FLOOR=%s, ROOMTYPE=%s WHERE ROOMNO=%s",
                (
                    self.var_floor.get(),
                    self.var_roomtype.get(),
                    self.var_roomno.get()
                )
            )
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Room details updated successfully", parent=self.root)

        #==============delete th existing data+======
    def deletefn(self):
        if self.var_floor.get() == "" or self.var_roomno.get() == "" or self.var_roomtype.get() == "":
            messagebox.showerror("Error", "Please enter a floor to delete.", parent=self.root)
            return
        deletefn = messagebox.askyesno("Hotel Management System", "Do you want to delete this room?", parent=self.root) 
        if deletefn:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="ROHIT@123", database="hotel11")
                mycursor = conn.cursor()
                query = "DELETE FROM roomdetails WHERE ROOMNO=%s"
                value = (self.var_roomno.get(),)
                mycursor.execute(query, value)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Deleted", "room deleted successfully!", parent=self.root)
                self.var_floor.set("")
                self.var_roomno.set("")
                self.var_roomtype.set("")
            except Exception as es:
                messagebox.showerror("Error", f"Error deleting data: {str(es)}", parent=self.root)


    def reset_data(self):
        self.var_floor.set("")
        self.var_roomno.set("")
        self.var_roomtype.set("")


if __name__ == "__main__":
    root = Tk()
    obj = dtroom(root)
    root.mainloop()