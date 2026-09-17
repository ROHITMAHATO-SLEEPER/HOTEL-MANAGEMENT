from tkinter import*
from PIL import Image,ImageTk   #pip install pillow
from cu import cust_win
from room3 import  roombk
from details import dtroom


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1540x800+0+0")


       #====================inst img==========================
        img1=Image.open(r"C:\Users\Rohit mahato\HMS IMAGE\hms11.png.jpg")
        img1=img1.resize((1550,140))
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        #===================logo=====================
        img2=Image.open(r"C:\Users\Rohit mahato\HMS IMAGE\logo.png")
        img2=img2.resize((230,140))
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        #===================TITLE==============
        lbl_title=Label(self.root,text="HOTEL MANAGEMEMT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="blue",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #====================main frame====================================
        mainframe=Frame(self.root,bd=4,relief=RIDGE)
        mainframe.place(x=0,y=190,width=1550,height=620)

        #=========menu============================
        lbl_menu=Label(mainframe,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="yellow",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

         #====================button frame====================================
        btnframe=Frame(mainframe,bd=4,relief=RIDGE)
        btnframe.place(x=0,y=35,width=228,height=150)

        custbtn=Button(btnframe,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="blue",bd=0,cursor="hand1")
        custbtn.grid(row=0,column=0,pady=1)

        roombtn=Button(btnframe,text="ROOM",command=self.rmbooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="blue",bd=0,cursor="hand1")
        roombtn.grid(row=1,column=0,pady=1)

        detbtn=Button(btnframe,text="DETAILS",command=self.rommdata,width=22,font=("times new roman",14,"bold"),bg="black",fg="blue",bd=0,cursor="hand1")
        detbtn.grid(row=2,column=0,pady=1)

        logbtn=Button(btnframe,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="blue",bd=0,cursor="hand1")
        logbtn.grid(row=4,column=0,pady=1)

        #============RIGHT SIDE IMAGE=============
        img3=Image.open(r"C:\Users\Rohit mahato\HMS IMAGE\MAINFRAME.jpg")
        img3=img3.resize((1310,590))
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(mainframe,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=225,y=0,width=1310,height=590)
       #====================down image==============
        img4=Image.open(r"C:\Users\Rohit mahato\HMS IMAGE\reception.jpg")
        img4=img4.resize((230,250))
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(mainframe,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=225,width=230,height=210)

        img5=Image.open(r"C:\Users\Rohit mahato\HMS IMAGE\image4.jpg")
        img5=img5.resize((230,190))
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg=Label(mainframe,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=420,width=230,height=190)
    
    def cust_details(self):
        self.newwin=Toplevel(self.root)
        self.app=cust_win(self.newwin)

    def rmbooking(self):
        self.newwin=Toplevel(self.root)
        self.app=roombk(self.newwin)

    def rommdata(self):
        self.newwin=Toplevel(self.root)
        self.app=dtroom(self.newwin)

    def logout(self):
        self.root.destroy()
    







if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()


