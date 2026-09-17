from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import random
from time import strftime
from datetime import datetime
class roombk:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # ========== Variables ==========
        self.var_contact = StringVar()
        self.var_checkindate = StringVar()
        self.var_checkoutdate = StringVar()
        self.var_roomtype = StringVar()
        self.var_availableroom = StringVar()
        self.var_no_ofdays = StringVar()
        self.var_meal = StringVar()
        self.var_paidtax = StringVar()
        self.var_subtotal = StringVar()
        self.var_totalcost = StringVar()

        # ========== Title ==========
        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("times new roman", 18, "bold"), bg="green", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        img2 = Image.open("C:/Users/Rohit mahato/HMS IMAGE/logo.png")
        img2 = img2.resize((100, 40))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=6, y=2, width=100, height=40)

        # ========== Room Details Frame ==========
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="ROOM DETAILS", padx=2, font=("times new roman", 12, "bold"))
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # ========== Form Fields ==========
        Label(labelframeleft, text="Customer contact:", font=("arial", 12, "bold")).grid(row=0, column=0, sticky=W, padx=2, pady=6)
        ttk.Entry(labelframeleft, textvariable=self.var_contact, width=20, font=("arial", 13, "bold")).grid(row=0, column=1, sticky=W)
        Button(labelframeleft, text="Fetch Data", command=self.fetchcontact, font=("arial", 10, "bold"), bg="blue", fg="yellow", width=8).place(x=346, y=4)

        Label(labelframeleft, text="Check_In Date:", font=("arial", 12, "bold")).grid(row=1, column=0, sticky=W, padx=2, pady=6)
        ttk.Entry(labelframeleft, textvariable=self.var_checkindate, width=29, font=("arial", 13, "bold")).grid(row=1, column=1,sticky=W)

        Label(labelframeleft, text="Check_Out Date:", font=("arial", 12, "bold")).grid(row=2, column=0, sticky=W, padx=2, pady=6)
        ttk.Entry(labelframeleft, textvariable=self.var_checkoutdate, width=29, font=("arial", 13, "bold")).grid(row=2, column=1,sticky=W)
        Label(labelframeleft, text="Room Type:", font=("arial", 12, "bold")).grid(row=3, column=0, sticky=W, padx=2, pady=6)
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="ROHIT@123", database="hotel11")
            mycursor = conn.cursor()
            mycursor.execute("SELECT DISTINCT ROOMTYPE FROM roomdetails")
            rrt = [row[0] for row in mycursor.fetchall()]
            conn.close()
        except Exception:
            rrt = []
        roomcombo = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype, width=29, font=("arial", 13, "bold"), state="readonly")
        roomcombo["values"] = rrt
        if rrt:
            roomcombo.current(0)
        roomcombo.grid(row=3, column=1, sticky=W, padx=2)

        Label(labelframeleft, text="Available Room:", font=("arial", 12, "bold")).grid(row=4, column=0, sticky=W, padx=2, pady=6)
        # Populate Available Room combobox from roomdetails table
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="ROHIT@123", database="hotel11")
            mycursor = conn.cursor()
            mycursor.execute("SELECT ROOMNO FROM roomdetails")
            rows = mycursor.fetchall()
            room_numbers = [row[0] for row in rows]
            conn.close()
        except Exception as e:
            room_numbers = []
        roomnocombo = ttk.Combobox(labelframeleft, textvariable=self.var_availableroom, width=29, font=("arial", 13, "bold"), state="readonly")
        roomnocombo["values"] = room_numbers
        if room_numbers:
            roomnocombo.current(0)
        roomnocombo.grid(row=4, column=1, sticky=W, padx=2)


        Label(labelframeleft, text="No Of Days:", font=("arial", 12, "bold")).grid(row=5, column=0, sticky=W, padx=2, pady=6)
        ttk.Entry(labelframeleft, textvariable=self.var_no_ofdays, width=29, font=("arial", 13, "bold")).grid(row=5, column=1)

        Label(labelframeleft, text="Meal:", font=("arial", 12, "bold")).grid(row=6, column=0, sticky=W, padx=2, pady=6)
        ttk.Entry(labelframeleft, textvariable=self.var_meal, width=29, font=("arial", 13, "bold")).grid(row=6, column=1)

        Label(labelframeleft, text="Paid Tax:", font=("arial", 12, "bold")).grid(row=7, column=0, sticky=W, padx=2, pady=6)
        ttk.Entry(labelframeleft, textvariable=self.var_paidtax, width=29, font=("arial", 13, "bold")).grid(row=7, column=1)

        Label(labelframeleft, text="Sub Total:", font=("arial", 12, "bold")).grid(row=8, column=0, sticky=W, padx=2, pady=6)
        ttk.Entry(labelframeleft, textvariable=self.var_subtotal, width=29, font=("arial", 13, "bold")).grid(row=8, column=1)

        Label(labelframeleft, text="Total Cost:", font=("arial", 12, "bold")).grid(row=9, column=0, sticky=W, padx=2, pady=6)
        ttk.Entry(labelframeleft, textvariable=self.var_totalcost, width=29, font=("arial", 13, "bold")).grid(row=9, column=1)

        # ==========  bill Buttons ==========
        Button(labelframeleft, text="BILL", command=self.total, font=("arial", 12, "bold"), bg="black", fg="gold", width=9).grid(row=10, column=0, padx=1, sticky=W)

        btnframe = Frame(labelframeleft, bd=2, relief=RIDGE)
        btnframe.place(x=0, y=400, width=412, height=40)

        Button(btnframe, text="ADD", command=self.add_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9).grid(row=0, column=0, padx=1)
        Button(btnframe, text="UPDATE",command=self.update ,font=("arial", 12, "bold"), bg="black", fg="gold", width=9).grid(row=0, column=1, padx=1)
        Button(btnframe, text="DELETE",command=self.deletefn ,font=("arial", 12, "bold"), bg="black", fg="gold", width=9).grid(row=0, column=2, padx=1)
        Button(btnframe, text="RESET",command=self.reset_data ,font=("arial", 12, "bold"), bg="black", fg="gold", width=9).grid(row=0, column=3, padx=1)

        # ========== Image ==========
        img3 = Image.open("C:/Users/Rohit mahato/HMS IMAGE/photo55.jpg")
        img3 = img3.resize((530, 300))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE).place(x=760, y=55, width=530, height=300)

        # ========== Search and Table ==========
        tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", padx=2, font=("times new roman", 12, "bold"))
        tableframe.place(x=435, y=280, width=860, height=260)

        Label(tableframe, font=("arial", 10, "bold"), text="Search By:", padx=2, pady=5, bg="red", fg="white").grid(row=0, column=0, sticky=W, padx=2)
        self.searchvar=StringVar()
        searchcombo = ttk.Combobox(tableframe,textvariable=self.searchvar ,font=("arial", 12, "bold"), width=24)
        searchcombo["values"] = ("Contact", "room")
        searchcombo.current(0)
        searchcombo.grid(row=0, column=1, padx=2)
  
        self.searchtxt=StringVar()
        ttk.Entry(tableframe,textvariable=self.searchtxt ,font=("arial", 13, "bold"), width=24).grid(row=0, column=2, padx=2)
        Button(tableframe, text="Search",command=self.search_data ,font=("arial", 12, "bold"), bg="gray", fg="gold", width=9).grid(row=0, column=3, padx=1)
        Button(tableframe, text="Show All",command=self.fetch_data, font=("arial", 12, "bold"), bg="gray", fg="gold", width=9).grid(row=0, column=4, padx=1)

        detframe = Frame(tableframe, bd=2, relief=RIDGE)
        detframe.place(x=0, y=50, width=860, height=180)

        scrollx = ttk.Scrollbar(detframe, orient=HORIZONTAL)
        scrolly = ttk.Scrollbar(detframe, orient=VERTICAL)

        self.roomtable = ttk.Treeview(detframe,
                                      columns=("Contact", "Check-in", "Check-out", "Roomtype", "AvailableRoom",
                                               "NoOfDays", "Meal"),
                                      xscrollcommand=scrollx.set,
                                      yscrollcommand=scrolly.set)
                                      

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.roomtable.xview)
        scrolly.config(command=self.roomtable.yview)
        self.roomtable.heading("Contact", text="Contact")
        self.roomtable.heading("Check-in", text="Check-in")
        self.roomtable.heading("Check-out", text="Check-out")
        self.roomtable.heading("Roomtype", text="Roomtype")
        self.roomtable.heading("AvailableRoom", text="AvailableRoom")
        self.roomtable.heading("NoOfDays", text="NoOfDays")
        self.roomtable.heading("Meal", text="Meal")
        for col in self.roomtable["columns"]:
            self.roomtable.heading(col, text=col)
            self.roomtable.column(col, width=100)

        self.roomtable["show"] = "headings"
        self.roomtable.pack(fill=BOTH, expand=1)
        self.roomtable.bind("<ButtonRelease-1>", self.getcursor)
        self.fetch_data()
# ===================add new data to  the system===================
    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkindate.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="ROHIT@123", database="hotel11")
                mycursor = conn.cursor()
                mycursor.execute("INSERT INTO roomd VALUES (%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_contact.get(),
                    self.var_checkindate.get(),
                    self.var_checkoutdate.get(),
                    self.var_roomtype.get(),
                    self.var_availableroom.get(),
                    self.var_no_ofdays.get(),
                    self.var_meal.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room Booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

#===============fetch data from database==============
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="ROHIT@123", database="hotel11")
            mycursor = conn.cursor()
            mycursor.execute("SELECT * FROM roomd")
            rows = mycursor.fetchall()
            if rows:
                self.roomtable.delete(*self.roomtable.get_children())
                for row in rows:
                    self.roomtable.insert("", END, values=row)
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error fetching data: {str(es)}", parent=self.root)

 #=================== getting data with the help of cursor=============
    def getcursor(self, event=""):
        cursor_row = self.roomtable.focus()
        content = self.roomtable.item(cursor_row)
        row = content["values"]
        self.var_contact.set(row[0])
        self.var_checkindate.set(row[1])
        self.var_checkoutdate.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_availableroom.set(row[4])
        self.var_no_ofdays.set(row[5])
        self.var_meal.set(row[6])
#=============function to upddate the existing details================
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="ROHIT@123", database="hotel11")
            mycursor = conn.cursor()
            mycursor.execute(
                "UPDATE roomd SET `Check-in`=%s, `Check-out`=%s, Roomtype=%s, AvailableRoom=%s, NoOfDays=%s, Meal=%s WHERE Contact=%s",
                (
                    self.var_checkindate.get(),
                    self.var_checkoutdate.get(),
                    self.var_roomtype.get(),
                    self.var_availableroom.get(),
                    self.var_no_ofdays.get(),
                    self.var_meal.get(),
                    self.var_contact.get()
                )
            )
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Room details updated successfully", parent=self.root)
    #==============delete th existing data+======
    def deletefn(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter a contact to delete.", parent=self.root)
            return
        deletefn = messagebox.askyesno("Hotel Management System", "Do you want to delete this booking?", parent=self.root) 
        if deletefn:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="ROHIT@123", database="hotel11")
                mycursor = conn.cursor()
                query = "DELETE FROM roomd WHERE Contact=%s"
                value = (self.var_contact.get(),)
                mycursor.execute(query, value)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Deleted", "Booking deleted successfully!", parent=self.root)
                self.var_contact.set("")
                self.var_checkindate.set("")
                self.var_checkoutdate.set("")
                self.var_roomtype.set("")
                self.var_availableroom.set("")
                self.var_no_ofdays.set("")
                self.var_meal.set("")
            except Exception as es:
                messagebox.showerror("Error", f"Error deleting data: {str(es)}", parent=self.root)

    def reset_data(self):
        self.var_contact.set("")
        self.var_checkindate.set("")
        self.var_checkoutdate.set("")
        self.var_roomtype.set("")
        self.var_availableroom.set("")
        self.var_no_ofdays.set("")
        self.var_meal.set("")
        self.var_paidtax.set("")
        self.var_subtotal.set("")
        self.var_totalcost.set("")


       




    def fetchcontact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter contact info.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="ROHIT@123", database="hotel11")
                mycursor = conn.cursor()
                query = "SELECT * FROM customer WHERE mobile=%s"
                value = (self.var_contact.get(),)
                mycursor.execute(query, value)
                row = mycursor.fetchall()

                if not row:
                    messagebox.showerror("Error", "Invalid Number.", parent=self.root)
                else:
                    showdataframe = LabelFrame(self.root, bd=4, relief=RIDGE, padx=2)
                    showdataframe.place(x=450, y=55, width=300, height=180)

                    Label(showdataframe, text="DETAILS:", font=("arial", 12, "bold")).place(x=0, y=0)
                    Label(showdataframe, text=f"Name: {row[0][1]}", font=("arial", 10)).place(x=0, y=30)
                    Label(showdataframe, text=f"Gender: {row[0][2]}", font=("arial", 10)).place(x=0, y=60)
                    Label(showdataframe, text=f"Nationality: {row[0][6]}", font=("arial", 10)).place(x=0, y=90)
                    Label(showdataframe, text=f"Address: {row[0][9]}", font=("arial", 10)).place(x=0, y=120)
                    Label(showdataframe, text=f"email: {row[0][5]}", font=("arial", 10)).place(x=0, y=150)

            except Exception as e:
                messagebox.showerror("Error", f"Database error: {str(e)}", parent=self.root)
            finally:
                if conn:
                    conn.close()


    def search_data(self):
        if self.searchvar.get() == "" or self.searchtxt.get() == "":
            messagebox.showerror("Error", "Please select a search criteria and enter search text", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="ROHIT@123", database="hotel11")
                mycursor = conn.cursor()
                query = f"SELECT * FROM roomd WHERE {self.searchvar.get()} LIKE %s"
                mycursor.execute(query, ('%' + self.searchtxt.get() + '%',))
                rows = mycursor.fetchall()
                if rows:
                       self.roomtable.delete(*self.roomtable.get_children())
                       for row in rows:
                           self.roomtable.insert("", END, values=row)
                else:
                    messagebox.showinfo("Info", "No matching records found", parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error during search: {str(es)}", parent=self.root)
        
# ========== Calculate Total Cost ==========

    def total(self):
        indate = self.var_checkindate.get()
        outdate = self.var_checkoutdate.get()
        indate_dt = datetime.strptime(indate, "%d/%m/%Y")
        outdate_dt = datetime.strptime(outdate, "%d/%m/%Y")
        self.var_no_ofdays.set(abs((outdate_dt - indate_dt).days))
        
        if (self.var_meal.get() == "Breakfast" or self.var_roomtype.get() == "Single"):
            q1 = float (1000)
            q2 = float(100)
            q3 =float(self.var_no_ofdays.get())
            q4 = float(q1+ q2) 
            q5= float(q3 + q4)
            Tax="Rs."+str("%.2f"%((q5)* 0.09))
            Subtotal="Rs."+str("%.2f"%(q5))
            Totalcost="Rs."+str("%.2f"%(q5 + (q5 * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(Subtotal)
            self.var_totalcost.set(Totalcost)

        elif (self.var_meal.get() == "Launch" or self.var_roomtype.get() == "Single"):
            q1 = float (1500)
            q2 = float(200)
            q3 =float(self.var_no_ofdays.get())
            q4 = float(q1+ q2) 
            q5= float(q3 + q4)
            Tax="Rs."+str("%.2f"%((q5)* 0.09))
            Subtotal="Rs."+str("%.2f"%(q5))
            Totalcost="Rs."+str("%.2f"%(q5 + (q5 * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(Subtotal)
            self.var_totalcost.set(Totalcost)    

        elif (self.var_meal.get() == "Dinner" or self.var_roomtype.get() == "single"):
            q1 = float (2000)
            q2 = float(300)
            q3 =float(self.var_no_ofdays.get())
            q4 = float(q1+ q2) 
            q5= float(q3 + q4)
            Tax="Rs."+str("%.2f"%((q5)* 0.09))
            Subtotal="Rs."+str("%.2f"%(q5))
            Totalcost="Rs."+str("%.2f"%(q5 + (q5 * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(Subtotal)
            self.var_totalcost.set(Totalcost)     
        elif (self.var_meal.get() == "Breakfast" or self.var_roomtype.get() == "Double"):
            q1 = float (2000)
            q2 = float(100)
            q3 =float(self.var_no_ofdays.get())
            q4 = float(q1+ q2) 
            q5= float(q3 + q4)
            Tax="Rs."+str("%.2f"%((q5)* 0.09))
            Subtotal="Rs."+str("%.2f"%(q5))
            Totalcost="Rs."+str("%.2f"%(q5 + (q5 * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(Subtotal)
            self.var_totalcost.set(Totalcost)       
        elif (self.var_meal.get() == "lanch" or self.var_roomtype.get() == "Double"):
            q1 = float (3000)
            q2 = float(500)
            q3 =float(self.var_no_ofdays.get())
            q4 = float(q1+ q2) 
            q5= float(q3 + q4)
            Tax="Rs."+str("%.2f"%((q5)* 0.09))
            Subtotal="Rs."+str("%.2f"%(q5))
            Totalcost="Rs."+str("%.2f"%(q5 + (q5 * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(Subtotal)
            self.var_totalcost.set(Totalcost) 
        elif (self.var_meal.get() == "Dinner" or self.var_roomtype.get() == "Double"):
            q1 = float (4000)
            q2 = float(500)
            q3 =float(self.var_no_ofdays.get())
            q4 = float(q1+ q2) 
            q5= float(q3 + q4)
            Tax="Rs."+str("%.2f"%((q5)* 0.09))
            Subtotal="Rs."+str("%.2f"%(q5))
            Totalcost="Rs."+str("%.2f"%(q5 + (q5 * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(Subtotal)
            self.var_totalcost.set(Totalcost)       
        elif (self.var_meal.get() == "Breakfast" or self.var_roomtype.get() == "Luxury"):
            q1 = float (2000)
            q2 = float(500)
            q3 =float(self.var_no_ofdays.get())
            q4 = float(q1+ q2) 
            q5= float(q3 + q4)
            Tax="Rs."+str("%.2f"%((q5)* 0.09))
            Subtotal="Rs."+str("%.2f"%(q5))
            Totalcost="Rs."+str("%.2f"%(q5 + (q5 * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(Subtotal)
            self.var_totalcost.set(Totalcost)
        elif (self.var_meal.get() == "" or self.var_roomtype.get() == "Luxury"):
            q1 = float (2000)
            q2 = float(500)
            q3 =float(self.var_no_ofdays.get())
            q4 = float(q1+ q2) 
            q5= float(q3 + q4)
            Tax="Rs."+str("%.2f"%((q5)* 0.09))
            Subtotal="Rs."+str("%.2f"%(q5))
            Totalcost="Rs."+str("%.2f"%(q5 + (q5 * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(Subtotal)
            self.var_totalcost.set(Totalcost)    

if __name__ == "__main__":
    root = Tk()
    obj = roombk(root)
    root.mainloop()