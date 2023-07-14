from tkinter import*
from tkinter import ttk  
from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
import mysql.connector


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()








class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\hp\Downloads\hbg.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450) 
        
        
        img1=Image.open(r"C:\Users\hp\Downloads\loginuser1.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
         
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100) 
        
        #label 
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155) 
        self.txtuser=ttk.Entry(frame,font=("times new roman",20,"bold"))
        self.txtuser.place(x=40,y=180,width=270)  
        username=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=225) 
        self.txtpass=ttk.Entry(frame,font=("times new roman",20,"bold"))
        self.txtpass.place(x=40,y=250,width=270) 
        
         
        #^^^^^^^^^^^^^^^^^^icon images^^^^^^^^^^^^^^^^^^^
        
        img2=Image.open(r"C:\Users\hp\Downloads\loginuser1.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25) 
        img3=Image.open(r"C:\Users\hp\Downloads\passicon.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=395,width=25,height=25) 
        
        #BUTTONS
        
        #login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",20,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        #register button
        registerbtn=Button(frame,command=self.rwin,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=20,y=350,width=160)
        
        #forget password  button
        fpbtn=Button(frame,command=self.forgot_password_window,text="Forgot Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        fpbtn.place(x=15,y=370,width=160)
        
         
    def rwin(self):
        self.new_window=Toplevel(self.root) #to open ur register window on toplevel
        self.app=Register(self.new_window)
         
    def login(self):
        if self.txtuser.get()==""or self.txtpass.get()=="":
             messagebox.showerror("Error","all fields required")
        elif self.txtuser.get()=="123" and self.txtpass.get()=="123":
             messagebox.showinfo("Success","Welcome",parent=self.root)
             self.new_window=Toplevel(self.root) #to open ur hsopital window on toplevel
             self.app=hospital( self.new_window)
             
             self.txtuser.delete(0,END)#to remove username after login 
             self.txtpass.delete(0,END)#to remove password after login
             
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="prerna098)(*",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
        
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("ERROR","Invalid Username & Password")
            else:
                op=messagebox.askyesno("YES/NO","ARE YOU ADMIN?")
                if op>0:
                    self.new_window=Toplevel(self.root)
                    self.app=hospital( self.new_window)
                    self.txtuser.delete(0,END)
                    self.txtpass.delete(0,END)
                else:
                    if not op:
                        return
            conn.commit()
            conn.close()  
            #messagebox.showerror("Invalid","Invalid username & password") 
            
            
    #*****************RESET PASSWORD *************************   
    def reset_pass(self):
        if self.combo_sq.get()=="Select":
            messagebox.showerror("Error","select the security question ",parent=self.root2) 
        elif self.txt_sa.get()=="":
            messagebox.showerror("Error","please enter something ",parent=self.root2) 
        elif self.new_pass.get()=="":
            messagebox.showerror("Error","please enter new password ",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="prerna098)(*",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_sq.get(),self.txt_sa.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("ERROR","enter the correct information",parent=self.root2)
            else:
                #UPDATION
                query=("update register set password=%s where email=%s")
                value=(self.new_pass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("INFO","PASSWORD HAS BEEN RESET",parent=self.root2)
                self.root2.destroy()
                
                
                
            
             
        
            
             
            
    #*****************FORGOT PASSWORD *************************
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("ERROR","Please enter the email to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="prerna098)(*",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("ERROR","This username doesn't exist!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),bg="white",fg="red")
                l.place(x=0,y=10,relwidth=1)
                
                sq=Label(self.root2,text="Select Security Question",font=("times new roman",16,"bold"),bg="white")
                sq.place(x=50,y=80)
                
                self.combo_sq=ttk.Combobox(self.root2,font=("timews new roman",16,"bold"),state="readonly")
                self.combo_sq["values"]=("Select","Your Birth Place","Your Bestfriend Name","Your Nickname")
                self.combo_sq.place(x=50,y=110,width=250)
                self.combo_sq.current(0)
                
               
               
                sa=Label(self.root2,text="Security Answer",font=("times new roman",16,"bold"),bg="white",fg="black")
                sa.place(x=50,y=150)
                
                self.txt_sa=ttk.Entry(self.root2,font=("times new roman",16,"bold"))
                self.txt_sa.place(x=50,y=180,width=250 )
                
                
                new_pass=Label(self.root2,text="New Password",font=("times new roman",16,"bold"),bg="white",fg="black")
                new_pass.place(x=50,y=220)
                
                self.new_pass=ttk.Entry(self.root2,font=("times new roman",16,"bold"))
                self.new_pass.place(x=50,y=250,width=250 )
                
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",16,"bold"),bg="green",fg="white")
                btn.place(x=50,y=290,width=250)
                
                
                        




class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1400x700+0+0")
        
        #TEXT VARIABLES
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        #***************BACKGROUND IMG **********************
        
        self.bg=ImageTk.PhotoImage(file=r"E:\miniproject\b111.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        #***************left IMG **********************
        
        self.bg1=ImageTk.PhotoImage(file=r"E:\miniproject\q1.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=300,height=500)
        
        
        ##################### Main FRame ###################
        frame=Frame(self.root,bg="white")
        frame.place(x=350,y=100,width=865,height=500)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl .place(x=20,y=20)
        
        
        #        label and entry 
        
        #ROW1
        fname=Label(frame,text="First Name",font=("times new roman",16,"bold"),bg="white")
        fname.place(x=50,y=100)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("timews new roman",16,"bold"))
        fname_entry.place(x=50,y=130,width=250)
        
        lname=Label(frame,text="Last Name",font=("times new roman",16,"bold"),bg="white",fg="black")
        lname.place(x=370,y=100)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",16,"bold"))
        self.txt_lname.place(x=370,y=130,width=250 )
        
        #ROW2
        contact=Label(frame,text="Contact No",font=("times new roman",16,"bold"),bg="white")
        contact.place(x=50,y=170)
        
        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("timews new roman",16,"bold"))
        contact_entry.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("times new roman",16,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)
        
        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",16,"bold"))
        email_entry.place(x=370,y=200,width=250 )
        
        #ROW3
        sq=Label(frame,text="Select Security Question",font=("times new roman",16,"bold"),bg="white")
        sq.place(x=50,y=240)
        
        self.combo_sq=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("timews new roman",16,"bold"),state="readonly")
        self.combo_sq["values"]=("Select","Your Birth Place","Your Bestfriend Name","Your Nickname")
        self.combo_sq.place(x=50,y=270,width=250)
        self.combo_sq.current(0)#select will be displaying
        
       
       
        sa=Label(frame,text="Security Answer",font=("times new roman",16,"bold"),bg="white",fg="black")
        sa.place(x=370,y=240)
        
        sa_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",16,"bold"))
        sa_entry.place(x=370,y=270,width=250 )
    
        #ROW4
        pas=Label(frame,text="Password",font=("times new roman",16,"bold"),bg="white")
        pas.place(x=50,y=310)
        
        pas_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("timews new roman",16,"bold"))
        pas_entry.place(x=50,y=340,width=250)
        
        cpas=Label(frame,text="Confirm password",font=("times new roman",16,"bold"),bg="white",fg="black")
        cpas.place(x=370,y=310)
        
        cpas_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",16,"bold"))
        cpas_entry.place(x=370,y=340,width=250 )
        
        
        #BUTTONS
        
        #login button
        img2=Image.open(r"E:\miniproject\l11.png")
        img2=img2.resize((200,60),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img2)
        b1=Button(frame,image=self.photoimage,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",16,"bold"),fg="white")
        b1.place(x=50,y=410,width=200)
        
        
        #register button
        img1=Image.open(r"E:\miniproject\12.jpg")
        img1=img1.resize((200,60))
        self.photoimage1=ImageTk.PhotoImage(img1) 
        b2=Button(frame,image=self.photoimage1,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",16,"bold"),fg="white")
        b2.place(x=370,y=410,width=200)
        
        
    
    #FUNCTIONALITY
    def register_data(self):
        if self.var_fname.get()=="" or self.var_pass.get()=="" or self.var_securityA.get()=="":
            messagebox.showerror("ERROR","All feilds are required",parent=self.root)
            
        
        elif  self.var_confpass.get()!=self.var_pass.get():
            messagebox.showerror("ERROR","Password must be same",parent=self.root)
        
        else:
            #messagebox.showinfo("SUCCESS","SUCCESSFULLY REGISTERED")
            conn=mysql.connector.connect(host="localhost",username="root",password="prerna098)(*",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("ERROR","User already exist!Try another email",parent=self.root)
                return
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                self.var_fname.get(),
                self.var_lname.get(),
                self.var_contact.get(),
                self.var_email.get(),
                self.var_securityQ.get(),
                self.var_securityA.get(),
                self.var_pass.get()
               ))
            conn.commit()
            conn.close()
            messagebox.showinfo("SUCCESS","SUCCESSFULLY REGISTERED")
        
    
    
    #to comeback to original login page if currently in registration page,fuctionality of login button in registration window
    def return_login(self):
        self.root.destroy()         
  
    
class hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("hospital management system")
        self.root.geometry("1540x800+0+0")



   


        #textvariables
        self.pname=StringVar() 
       
        self.dob=StringVar()
        self.pa=StringVar()
   
        self.no=StringVar()
        self.refno=StringVar()
        self.dose=StringVar()
        self.notb=StringVar()
        self.id=StringVar()
        self.expdate=StringVar()
        self.dd=StringVar()
        self.se=StringVar() 

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="white",bg="darkgreen",font=("times new roman",40,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #dataframe
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=100,width=1275,height=300)

        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Patient Info",bg="pink")
        DataframeLeft.place(x=0,y=5,width=800,height=255)
        
        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Prescription",bg="beige")
        DataframeRight.place(x=805,y=5,width=415,height=255)



        #buttons frame

        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=588,width=1270,height=75)

        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=400,width=1270,height=215)

       # DataframeLeft

        lblpatientname=Label(DataframeLeft,text="Patient Name",font=("times new roman",12,"bold"),padx=2,pady=6,bg="pink")
        lblpatientname.grid(row=0,column=0,sticky=W)
        txtpname=Entry(DataframeLeft,textvariable=self.pname,font=("arial",12,"bold"),width=20)
        txtpname.grid(row=0,column=2)

        lbldob=Label(DataframeLeft,text="Date of birth",font=("times new roman",12,"bold"),padx=2,pady=6,bg="pink")
        lbldob.grid(row=1,column=0)
        txtdob=Entry(DataframeLeft,textvariable=self.dob,font=("arial",12,"bold"),width=20)
        txtdob.grid(row=1,column=2)
        

        lbladdr=Label(DataframeLeft,text="Patient Address",font=("times new roman",12,"bold"),padx=2,pady=6,bg="pink")
        lbladdr.grid(row=2,column=0)
        txtaddr=Entry(DataframeLeft,textvariable=self.pa,font=("arial",12,"bold"),width=20)
        txtaddr.grid(row=2,column=2)

        lblno=Label(DataframeLeft,text="Name of Tablet",font=("times new roman",12,"bold"),padx=2,pady=6,bg="pink")
        lblno.grid(row=3,column=0)
        txtno=Entry(DataframeLeft,textvariable=self.no,font=("arial",12,"bold"),width=20)
        txtno.grid(row=3,column=2)

        lblrefno=Label(DataframeLeft,text="Reference no",font=("times new roman",12,"bold"),padx=2,pady=6,bg="pink")
        lblrefno.grid(row=4,column=0)
        txtref=Entry(DataframeLeft,textvariable=self.refno,font=("arial",12,"bold"),width=20)
        txtref.grid(row=4,column=2)

        lbldosage=Label(DataframeLeft,text="Dosage",font=("times new roman",12,"bold"),padx=2,pady=6,bg="pink")
        lbldosage.grid(row=5,column=0)
        txtdos=Entry(DataframeLeft,textvariable=self.dose,font=("arial",12,"bold"),width=20)
        txtdos.grid(row=5,column=2)

        lblnumber=Label(DataframeLeft,text="No. of Tablets",font=("times new roman",12,"bold"),padx=2,pady=6,bg="pink")
        lblnumber.grid(row=0,column=11)
        txtn=Entry(DataframeLeft,textvariable=self.notb,font=("arial",12,"bold"),width=20)
        txtn.grid(row=0,column=12)

        lblid=Label(DataframeLeft,text="Issue date",font=("times new roman",12,"bold"),padx=2,pady=6,bg="pink")
        lblid.grid(row=1,column=11)
        txtid=Entry(DataframeLeft,textvariable=self.id,font=("arial",12,"bold"),width=20)
        txtid.grid(row=1,column=12)

        lblexp=Label(DataframeLeft,text="Expiry date",font=("times new roman",12,"bold"),padx=2,pady=6,bg="pink")
        lblexp.grid(row=2,column=11)
        txtexp=Entry(DataframeLeft,textvariable=self.expdate,font=("arial",12,"bold"),width=20)
        txtexp.grid(row=2,column=12)

        lbldd=Label(DataframeLeft,text="daily dosage",font=("times new roman",12,"bold"),padx=2,pady=6,bg="pink")
        lbldd.grid(row=3,column=11)
        txtdd=Entry(DataframeLeft,textvariable=self.dd,font=("arial",12,"bold"),width=20)
        txtdd.grid(row=3,column=12)

        lblse=Label(DataframeLeft,text="Side Effect",font=("times new roman",12,"bold"),padx=2,pady=6,bg="pink")
        lblse.grid(row=4,column=11)
        txtse=Entry(DataframeLeft,textvariable=self.se,font=("arial",12,"bold"),width=20)
        txtse.grid(row=4,column=12)

        

        #dataframe right
        self.txtprescription=Text(DataframeRight,font=("arial",12,"bold"),width=40,height=11,padx=2,pady=6,bg="beige")
        self.txtprescription.grid(row=0,column=0)

        #buttons

        btnprescription=Button(Buttonframe,text="Prescription",command=self.iprescription,bg="green",fg="white",font=("arial",12,"bold"),width=20,height=1,padx=2,pady=6)
        btnprescription.grid(row=0,column=0)

        btnprescriptiondata=Button(Buttonframe,text="Prescription Data",command=self.iprescriptionData,bg="green",fg="white",font=("arial",12,"bold"),width=20,height=1,padx=2,pady=6)
        btnprescriptiondata.grid(row=0,column=1)

        btnupdate=Button(Buttonframe,text="Update",command=self.update,bg="green",fg="white",font=("arial",12,"bold"),width=20,height=1,padx=2,pady=6)
        btnupdate.grid(row=0,column=2)

        btnDel=Button(Buttonframe,text="Delete",command=self.Delete,bg="green",fg="white",font=("arial",12,"bold"),width=20,height=1,padx=2,pady=6)
        btnDel.grid(row=0,column=3)

        btnclear=Button(Buttonframe,text="Clear",command=self.clear,bg="green",fg="white",font=("arial",12,"bold"),width=20,height=1,padx=2,pady=6)
        btnclear.grid(row=0,column=4)

        
        btnexit=Button(Buttonframe,text="Exit",command=self.exit,bg="green",fg="white",font=("arial",12,"bold"),width=16,height=1,padx=2,pady=6)
        btnexit.grid(row=0,column=5)

        #SCROLLBAR
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("Patient Name","DOB","Patient Address","Name of Tablets","Reference No.","Dosage","No. of Tablets","Issue Date","Expiry Date","Daily Dose","Side Effect"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("Patient Name",text="Patient Name")
        self.hospital_table.heading("DOB",text="DOB")
        self.hospital_table.heading("Patient Address",text="Patient Address")
        self.hospital_table.heading("Name of Tablets",text="Name of Tablets")
        self.hospital_table.heading("Reference No.",text="Reference No.")
        self.hospital_table.heading("Dosage",text="Dosage")
        self.hospital_table.heading("No. of Tablets",text="No. of Tablets")
        self.hospital_table.heading("Issue Date",text="Issue Date")
        self.hospital_table.heading("Expiry Date",text="Expiry Date")
        self.hospital_table.heading("Daily Dose",text="Daily Dose")
        self.hospital_table.heading("Side Effect",text="Side Effect")

        self.hospital_table["show"]="headings"
  

        self.hospital_table.column("Patient Name",width=80)
        self.hospital_table.column("DOB",width=80)
        self.hospital_table.column("Patient Address",width=80)
        self.hospital_table.column("Name of Tablets",width=80)
        self.hospital_table.column("Reference No.",width=80)
        self.hospital_table.column("Dosage",width=80)
        self.hospital_table.column("No. of Tablets",width=80)
        self.hospital_table.column("Issue Date",width=80)
        self.hospital_table.column("Expiry Date",width=80)
        self.hospital_table.column("Daily Dose",width=80)
        self.hospital_table.column("Side Effect",width=80)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()






             #functionality
    def iprescriptionData(self):
        if self.notb.get()=="" or self.refno.get()=="":
             messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="prerna098)(*",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.pname.get(),
                                                                                        self.dob.get(), 
                                                                                        self.pa.get(),
                                                                                        self.no.get(),
                                                                                        self.refno.get(),
                                                                                        self.dose.get(),
                                                                                        self.notb.get(),
                                                                                        self.id.get(),
                                                                                        self.expdate.get(),
                                                                                        self.dd.get(),
                                                                                        self.se.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted",parent=self.root)

    #display the records inserted in interface
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="prerna098)(*",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
                conn.commit()
            conn.close()

    #to diplsay the details in leftdrame of slelected records
    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.pname.set(row[0])  
        self.dob.set(row[1])
        self.pa.set(row[2])
        self.no.set(row[3])
        self.refno.set(row[4])
        self.dose.set(row[5])
        self.notb.set(row[6])
        self.id.set(row[7])
        self.expdate.set(row[8])
        self.dd.set(row[9])
        self.se.set(row[10])    
        



    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="prerna098)(*",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set NameofTablets=%s,Dose=%s,NoofTablets=%s,IssueDate=%s,ExpDate=%s,DailyDose=%s,SideEffect=%s,PatientName=%s,DOB=%s,PatientAddress=%s where Reference=%s",(
                            self.no.get(),
                            self.dose.get(),
                            self.notb.get(),
                            self.id.get(),
                            self.expdate.get(),
                            self.dd.get(),
                            self.se.get(),
                            self.pname.get(),
                            self.dob.get(),
                            self.pa.get(),
                            self.refno.get(),
                ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("update","record has been updated successfully",parent=self.root)

    def iprescription(self):
        self.txtprescription.insert(END,"patient name:\t\t\t"+self.pname.get()+"\n")
        self.txtprescription.insert(END,"DOB:\t\t\t"+self.dob.get()+"\n")
        self.txtprescription.insert(END,"Patient Address:\t\t\t"+self.pa.get()+"\n")
        self.txtprescription.insert(END,"Name of Tablets:\t\t\t"+self.no.get()+"\n")
        self.txtprescription.insert(END,"Reference No:\t\t\t"+self.refno.get()+"\n")
        self.txtprescription.insert(END,"Dosage:\t\t\t"+self.dose.get()+"\n")
        self.txtprescription.insert(END,"No. of Tablets:\t\t\t"+self.notb.get()+"\n")
        self.txtprescription.insert(END,"Issue Date:\t\t\t"+self.id.get()+"\n")
        self.txtprescription.insert(END,"Expiry Date:\t\t\t"+self.expdate.get()+"\n")
        self.txtprescription.insert(END,"Daily Dose:\t\t\t"+self.dd.get()+"\n")
        self.txtprescription.insert(END,"Side Effect:\t\t\t"+self.se.get()+"\n")


    def Delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="prerna098)(*",database="mydata")
        my_cursor=conn.cursor()
        query="delete from hospital where Reference=%s"
        value=(self.refno.get(),)
        my_cursor.execute(query,value)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","deleted successfully",parent=self.root)


    def clear(self):
        self.pname.set('') 
        self.dob.set('') 
        self.pa.set('') 
        self.no.set('') 
        self.refno.set('') 
        self.dose.set('') 
        self.notb.set('') 
        self.id.set('') 
        self.expdate.set('') 
        self.dd.set('') 
        self.se.set('')
        self.txtprescription.delete("1.0",END)


    def exit(self):
        exit=messagebox.askyesno("hospital management system","Confirm your exit",parent=self.root)
        if(exit>0):
            self.root.destroy()
            return









    
    
if __name__ == "__main__":
    main()