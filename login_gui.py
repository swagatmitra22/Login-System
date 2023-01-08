from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk

class Login_System:
  def __init__(self,root):
    self.root=root
    self.root.title("Login System | Developed by Swagat Mitra | 22BAI1400")
    self.root.geometry("1230x500+150+140")
    self.root.config(bg="old lace")
    self.logo=ImageTk.PhotoImage(file="C:\\Users\\swaga\\Downloads\\logo.png")

    title=Label(self.root,text='AASWANI THERMALS PVT. LTD.',font=("cambria",35,"bold"),bg="DodgerBlue4",fg="white",padx=10)
    title.place(x=0,y=0,relwidth=1)

    #=============IMAGE FRAME==============
    logo_frame=Frame(self.root,bg="white")
    logo_frame.place(x=20,y=62)

    logo_lbl=Label(logo_frame,image=self.logo,bg='old lace').grid()

    #==============VARIABLES================
    self.uname=StringVar()
    self.passwd=StringVar()

    #=============LOGIN WINDOW==============
    login=Frame(self.root,bd=5,relief=RIDGE,bg="white")        
    login.place(x=555,y=75,width=650,height=410)
    title1=Label(login,text="USER LOGIN",font=("cambria",25,"bold"),bg="firebrick3",fg="yellow",anchor='w',padx=10).place(x=0,y=0,relwidth=1)

    lbluser=Label(login,text="Username :",font=("cambria",20,"bold"),bg="white",fg="black").place(x=15,y=130)
    txtuser=Entry(login,textvariable=self.uname,bd=3,font=("cambria",20),bg="light yellow",fg="black").place(x=200,y=130,width=400)
       
    lblpass=Label(login,text="Password :",font=("cambria",20,"bold"),bg="white",fg="black").place(x=15,y=200)
    txtpass=Entry(login,textvariable=self.passwd,bd=3,font=("cambria",20),show="*",bg="light yellow",fg="black").place(x=200,y=200,width=400)
    

    btn_login=Button(login,text="  LOGIN  ",command=self.login,font=("cambria",20),bg="green3",fg="black",width=12,height=1).place(x=410,y=300)

  def login(self):
    if self.uname.get()=="" or self.passwd.get()=="":
      messagebox.showerror("ERROR","All fields are required !!")
    elif self.uname.get()=="admin" and self.passwd.get()=="12345678":
      messagebox.showinfo("SUCCESSFUL",F"Welcome {self.uname.get()}")
    else:
      messagebox.showerror("ERROR","Invalid Username or Password !!")
          
root=Tk()
obj=Login_System(root)
root.mainloop()