from tkinter import*
from PIL import Image,ImageTk   #pip install pillow
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System - Register")
        self.root.geometry("1550x800+0+0")

        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()
        self.var_security_question = StringVar()
        self.var_answer = StringVar()
        # Background Image
        self.bg_image = Image.open(r"C:\Users\Rohit mahato\Downloads\reg33.png")
        self.bg_image = self.bg_image.resize((1550, 800))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        bg_label = Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.bg_image2 = Image.open(r"C:\Users\Rohit mahato\Downloads\reg44.png")
        self.bg_image2 = self.bg_image2.resize((400, 450))
        self.bg_photo2 = ImageTk.PhotoImage(self.bg_image2)
        bg_label2 = Label(self.root, image=self.bg_photo2, bd=0, relief=RIDGE)
        bg_label2.place(x=50, y=100, width=470, height=550)
        #frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        # Title
        title_label = Label(frame, text="Register Here", font=("times new roman", 30, "bold"), bg="white", fg="green")
        title_label.place(x=20, y=20)
        # Username Label and Entry
        username_label = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        username_label.place(x=50, y=100)
        self.first_name_entry = ttk.Entry(frame,textvariable=self.var_first_name,font=("times new roman", 15, "bold"), width=20)
        self.first_name_entry.place(x=50, y=140, width=250)
        # Last Name Label and Entry
        last_name_label = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        last_name_label.place(x=400, y=100)
        self.last_name_entry = ttk.Entry(frame,textvariable=self.var_last_name ,font=("times new roman", 15, "bold"), width=20)
        self.last_name_entry.place(x=400, y=140, width=250)
        #contact Label and Entry
        contact_label = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        contact_label.place(x=50, y=180)
        self.contact_entry = ttk.Entry(frame,textvariable=self.var_contact ,font=("times new roman", 15, "bold"), width=20)
        self.contact_entry.place(x=50, y=220, width=250)
        # Email Label and Entry
        email_label = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email_label.place(x=400, y=180)
        self.email_entry = ttk.Entry(frame,textvariable=self.var_email ,font=("times new roman", 15, "bold"), width=20)
        self.email_entry.place(x=400, y=220, width=250)
        # Password Label and Entry
        password_label = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        password_label.place(x=50, y=260)
        self.password_entry = ttk.Entry(frame,textvariable=self.var_password ,font=("times new roman", 15, "bold"), show="*", width=20)
        self.password_entry.place(x=50, y=300, width=250)
        # Confirm Password Label and Entry
        confirm_password_label = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        confirm_password_label.place(x=400, y=260)
        self.confirm_password_entry = ttk.Entry(frame,textvariable=self.var_confirm_password ,font=("times new roman", 15, "bold"), show="*", width=20)
        self.confirm_password_entry.place(x=400, y=300, width=250)
        #security question Label and Entry
        security_question_label = Label(frame, text="Security Question", font=("times new roman", 15, "bold"), bg="white")
        security_question_label.place(x=50, y=340)
        self.security_question_combobox = ttk.Combobox(frame,textvariable=self.var_security_question ,font=("times new roman", 15, "bold"), width=18, state='readonly')
        self.security_question_combobox['values'] = ("Select", "Your Birth Place", "Your Pet Name", "Your Best Friend Name")
        self.security_question_combobox.place(x=50, y=380, width=250)
        self.security_question_combobox.current(0)
        # Answer Label and Entry
        answer_label = Label(frame, text="Answer", font=("times new roman", 15, "bold"), bg="white")
        answer_label.place(x=400, y=340)
        self.answer_entry = ttk.Entry(frame,textvariable=self.var_answer ,font=("times new roman", 15, "bold"), width=20)
        self.answer_entry.place(x=400, y=380, width=250)
        #checkbox
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, text="I Agree to the Terms and Conditions", variable=self.var_check, onvalue=1, offvalue=0, font=("times new roman", 12, "bold"), bg="white", fg="black")
        checkbtn.place(x=50, y=420, width=300)
        
        # Register Button
        register_btn = Button(frame, text="Register", font=("times new roman", 15, "bold"), bg="green", fg="white", command=self.register_user)
        register_btn.place(x=110, y=450, width=150, height=40)
        #login Button
        login_btn = Button(frame, text="Login", font=("times new roman", 15, "bold"), bg="darkblue", fg="white",)
        login_btn.place(x=500, y=450, width=150, height=40)


    def register_user(self):
        first_name = self.var_first_name.get()
        last_name = self.var_last_name.get()
        contact = self.var_contact.get()
        email = self.var_email.get()
        password = self.var_password.get()
        confirm_password = self.var_confirm_password.get()
        security_question = self.var_security_question.get()
        answer = self.var_answer.get()

        if (first_name == "" or last_name == "" or contact == "" or email == "" or
            password == "" or confirm_password == "" or security_question == "Select" or answer == ""):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match", parent=self.root)
            return
        if self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to the Terms and Conditions", parent=self.root)
            return

        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="ROHIT@123", database="hotel11")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
            row = cursor.fetchone()
            if row:
                messagebox.showerror("Error", "User already exists, please try another email", parent=self.root)
            else:
                cursor.execute(
                    "INSERT INTO users (first_name, last_name, contact, email, password, security_question, answer) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (first_name, last_name, contact, email, password, security_question, answer)
                )
                conn.commit()
                messagebox.showinfo("Success", "Registration successful", parent=self.root)
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Database error: {str(es)}", parent=self.root)



        
if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()

