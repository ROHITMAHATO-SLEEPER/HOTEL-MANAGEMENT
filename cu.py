from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class cust_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # ===================== Variables ====================
        self.var_ref = StringVar()
        x = random.randint(1000, 99999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_adderss = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()

        # ======== Title ==========
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="gray", fg="blue", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ========== Logo ==========
        img2 = Image.open("C:/Users/Rohit mahato/HMS IMAGE/logo.png")
        img2 = img2.resize((100, 40))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=6, y=2, width=100, height=40)

        # =========== Label Frame ============
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", padx=2, font=("times new roman", 12, "bold"))
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # ========== Labels and Entries ==========
        Label(labelframeleft, text="Customer Ref", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=0, column=0, sticky=W)
        ttk.Entry(labelframeleft, textvariable=self.var_ref, width=29, font=("arial", 13, "bold"), state="readonly").grid(row=0, column=1)

        Label(labelframeleft, text="Customer Name", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=1, column=0, sticky=W)
        ttk.Entry(labelframeleft, textvariable=self.var_cust_name, font=("arial", 13, "bold"), width=29).grid(row=1, column=1)

        Label(labelframeleft, text="Gender", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=3, column=0, sticky=W)
        gencombo = ttk.Combobox(labelframeleft, textvariable=self.var_gender, font=("arial", 12, "bold"), width=27, state="readonly")
        gencombo["value"] = ("Male", "Female", "Others")
        gencombo.current(0)
        gencombo.grid(row=3, column=1)

        Label(labelframeleft, text="PostCode", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=4, column=0, sticky=W)
        ttk.Entry(labelframeleft, textvariable=self.var_post, font=("arial", 13, "bold"), width=29).grid(row=4, column=1)

        Label(labelframeleft, text="Mobile", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=5, column=0, sticky=W)
        ttk.Entry(labelframeleft, textvariable=self.var_mobile, font=("arial", 13, "bold"), width=29).grid(row=5, column=1)

        Label(labelframeleft, text="Email", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=6, column=0, sticky=W)
        ttk.Entry(labelframeleft, textvariable=self.var_email, font=("arial", 13, "bold"), width=29).grid(row=6, column=1)

        Label(labelframeleft, text="Nationality", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=7, column=0, sticky=W)
        nationcom = ttk.Combobox(labelframeleft, textvariable=self.var_nationality, font=("arial", 12, "bold"), width=27, state="readonly")
        nationcom["value"] = ("Indian", "Nepali", "American")
        nationcom.current(0)
        nationcom.grid(row=7, column=1)

        Label(labelframeleft, text="Id Proof Type", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=8, column=0, sticky=W)
        idcombo = ttk.Combobox(labelframeleft, textvariable=self.var_id_proof, font=("arial", 12, "bold"), width=27, state="readonly")
        idcombo["value"] = ("Adhar card", "Driving license", "Passport")
        idcombo.current(0)
        idcombo.grid(row=8, column=1)

        Label(labelframeleft, text="Id Number", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=9, column=0, sticky=W)
        ttk.Entry(labelframeleft, textvariable=self.var_id_number, font=("arial", 13, "bold"), width=29).grid(row=9, column=1)

        Label(labelframeleft, text="Address", font=("arial", 12, "bold"), padx=2, pady=6).grid(row=10, column=0, sticky=W)
        ttk.Entry(labelframeleft, textvariable=self.var_adderss, font=("arial", 13, "bold"), width=29).grid(row=10, column=1)

        # ========== Buttons ==========
        btnframe = Frame(labelframeleft, bd=2, relief=RIDGE)
        btnframe.place(x=0, y=400, width=412, height=40)

        Button(btnframe, text="ADD", command=self.add_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9).grid(row=0, column=0, padx=1)
        Button(btnframe, text="UPDATE", command=self.update, font=("arial", 12, "bold"), bg="black", fg="gold", width=9).grid(row=0, column=1, padx=1)
        Button(btnframe, text="DELETE",command=self.deletefn ,font=("arial", 12, "bold"), bg="black", fg="gold", width=9).grid(row=0, column=2, padx=1)
        Button(btnframe, text="RESET", command=self.reset_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9).grid(row=0, column=3, padx=1)

        # ========== Table View ==========
        tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", padx=2, font=("times new roman", 12, "bold"))
        tableframe.place(x=435, y=50, width=860, height=490)

        Label(tableframe, font=("arial", 12, "bold"), text="SearchBy:", padx=2, pady=6, bg="red", fg="white").grid(row=0, column=0, sticky=W, padx=2)
        self.searchvar=StringVar()
        searchcombo = ttk.Combobox(tableframe,textvariable=self.searchvar,font=("arial", 12, "bold"), width=24, state="readonly")
        searchcombo["value"] = ("mobile", "ref_no", "idnumber")
        searchcombo.current(0)
        searchcombo.grid(row=0, column=1, padx=2)
        self.searchtxt=StringVar()
        ttk.Entry(tableframe,font=("arial", 13, "bold"),textvariable=self.searchtxt ,width=24).grid(row=0, column=2, padx=2)
        Button(tableframe, text="Search",command=self.search_data,font=("arial", 12, "bold"), bg="gray", fg="gold", width=9).grid(row=0, column=3, padx=1)
        Button(tableframe, text="show all" ,command=self.fetch_data,font=("arial", 12, "bold"), bg="gray", fg="gold", width=9).grid(row=0, column=4, padx=1)

        # ========== Data Table ==========
        detframe = Frame(tableframe, bd=2, relief=RIDGE)
        detframe.place(x=0, y=50, width=860, height=350)

        scrollx = ttk.Scrollbar(detframe, orient=HORIZONTAL)
        scrolly = ttk.Scrollbar(detframe, orient=VERTICAL)

        self.cust_details = ttk.Treeview(detframe, column=("Customer ref", "Customer Name", "Gender", "PostCode", "Mobile", "Email",
                                                           "Nationality", "Id Proof Type", "Id Number", "Address"),
                                         xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.cust_details.xview)
        scrolly.config(command=self.cust_details.yview)

        self.cust_details.heading("Customer ref", text="ref_no")
        self.cust_details.heading("Customer Name", text="name")
        self.cust_details.heading("Gender", text="gender")
        self.cust_details.heading("PostCode", text="postcode")
        self.cust_details.heading("Mobile", text="mobile")
        self.cust_details.heading("Email", text="email")
        self.cust_details.heading("Nationality", text="nationality")
        self.cust_details.heading("Id Proof Type", text="idproof")
        self.cust_details.heading("Id Number", text="idnumber")
        self.cust_details.heading("Address", text="address")

        self.cust_details["show"] = "headings"
        for col in self.cust_details["columns"]:
            self.cust_details.column(col, width=100)

        self.cust_details.pack(fill=BOTH, expand=1)
        self.cust_details.bind("<ButtonRelease-1>", self.getcursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get() == "" or self.var_id_number.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="ROHIT@123", database="hotel11")
                mycursor = conn.cursor()
                mycursor.execute("INSERT INTO customer VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_adderss.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="ROHIT@123", database="hotel11")
            mycursor = conn.cursor()
            mycursor.execute("SELECT * FROM customer")
            rows = mycursor.fetchall()
            if rows:
                self.cust_details.delete(*self.cust_details.get_children())
                for row in rows:
                    self.cust_details.insert("", END, values=row)
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error fetching data: {str(es)}", parent=self.root)

    def getcursor(self, event=""):
        cursor_row = self.cust_details.focus()
        content = self.cust_details.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_gender.set(row[2])
        self.var_post.set(row[3])
        self.var_mobile.set(row[4])
        self.var_email.set(row[5])
        self.var_nationality.set(row[6])
        self.var_id_proof.set(row[7])
        self.var_id_number.set(row[8])
        self.var_adderss.set(row[9])

    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="ROHIT@123", database="hotel11")
            mycursor = conn.cursor()
            mycursor.execute("UPDATE customer SET name=%s, gender=%s, postcode=%s, mobile=%s, email=%s, nationality=%s, idproof=%s, idnumber=%s, address=%s WHERE ref_no=%s", (
                self.var_cust_name.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_adderss.get(),
                self.var_ref.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Customer details updated successfully", parent=self.root)

    def deletefn(self):
     deletefn = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer?", parent=self.root) 
     if deletefn:
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="ROHIT@123", database="hotel11")
            mycursor = conn.cursor()
            query = "DELETE FROM customer WHERE ref_no=%s"
            value = (self.var_ref.get(),)
            mycursor.execute(query, value)
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Deleted", "Customer deleted successfully!", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Error deleting data: {str(es)}", parent=self.root)


    def search_data(self):
        if self.searchvar.get() == "" or self.searchtxt.get() == "":
            messagebox.showerror("Error", "Please select a search criteria and enter search text", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="ROHIT@123", database="hotel11")
                mycursor = conn.cursor()
                query = f"SELECT * FROM customer WHERE {self.searchvar.get()} LIKE %s"
                mycursor.execute(query, ('%' + self.searchtxt.get() + '%',))
                rows = mycursor.fetchall()
                if rows:
                       self.cust_details.delete(*self.cust_details.get_children())
                       for row in rows:
                           self.cust_details.insert("", END, values=row)
                else:
                    messagebox.showinfo("Info", "No matching records found", parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error during search: {str(es)}", parent=self.root)
        



               

    def reset_data(self):
        self.var_cust_name.set("")
        self.var_gender.set("Male")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_nationality.set("Indian")
        self.var_adderss.set("")
        self.var_id_proof.set("Adhar card")
        self.var_id_number.set("")
        x = random.randint(1000, 99999)
        self.var_ref.set(str(x))
     


if __name__ == "__main__":
    root = Tk()
    obj = cust_win(root)
    root.mainloop()
