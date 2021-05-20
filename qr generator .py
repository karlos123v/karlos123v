from tkinter import*
import mysql.connector as m
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage

class Qr_codegenerator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR_Code Generator |developed by MS coproration")
        self.root.resizable(False,False)

        title=Label(self.root,text="                  Qr_code Generator",font=("times new roman",40),bg='#053746',fg='white',anchor='w').place(x=0,y=0,relwidth=1)
        # employee detail window
        # VAriable
        self.var_stu_roll=StringVar()
        self.var_stu_name=StringVar()
        self.var_stu_class=StringVar()
        self.var_stu_sub=StringVar()
        emp_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_frame.place(x=50,y=100,width=500,height=380)
        #-----------------------------------------------------label is display student name--------------------------------------------------
        
        title=Label(emp_frame,text="Student Details",font=("goudy old style",20),bg='#053746',fg='white').place(x=0,y=0,relwidth=1)
        stu_roll=Label(emp_frame,text="Student Rollno",font=("timesnew roman",15,'bold'),bg='white',fg='black',anchor='w').place(x=20,y=60,relwidth=1)
        stu_name=Label(emp_frame,text="Student Name",font=("timesnew roman",15,'bold'),bg='white',fg='black',anchor='w').place(x=20,y=100,relwidth=1)
        stu_class=Label(emp_frame,text="Student class",font=("timesnew roman",15,'bold'),bg='white',fg='black',anchor='w').place(x=20,y=140,relwidth=1)
        stu_subject=Label(emp_frame,text="Student subject",font=("timesnew roman",15,'bold'),bg='white',fg='black',anchor='w').place(x=20,y=180,relwidth=1)
#---------------------------------------------------------------Entry is used to input data-------------------------------------------------------------------------
        txt_stu_roll=Entry(emp_frame,textvariable=self.var_stu_roll,font=("timesnew roman",15,'bold'),bg='lightyellow').place(x=200,y=60)
        txt_stu_name=Entry(emp_frame,textvariable=self.var_stu_name,font=("timesnew roman",15,'bold'),bg='lightyellow').place(x=200,y=100)
        txt_stu_class=Entry(emp_frame,textvariable=self.var_stu_class,font=("timesnew roman",15,'bold'),bg='lightyellow').place(x=200,y=140)
        txt_stu_subject=Entry(emp_frame,textvariable=self.var_stu_sub,font=("timesnew roman",15,'bold'),bg='lightyellow').place(x=200,y=180)
        #--------------------------------------------------------button is used to take command from the user and perform various operation-----------------------------------------------------------------------
        btn_stu=Button(emp_frame,text="Generate QR code",font=("times new roman",15,'bold'),command=self.generate,bg='blue',fg='white').place(x=90,y=250,width=180,height=30)
        btn_stu=Button(emp_frame,text="Clear",command=self.clear, font=("times new roman",15,'bold'),bg='grey',fg='white').place(x=300,y=250,width=120,height=30)
        btn_stu_submit=Button(emp_frame,text="Submit", command=self.Submit,font=("times new roman",15,'bold'),bg='red',fg='white').place(x=160,y=330,width=120,height=30)
        btn_stu_submit=Button(emp_frame,text="new page", command=self.change,font=("times new roman",15,'bold'),bg='grey',fg='white').place(x=300,y=330,width=120,height=30)
        self.msg=""
        self.lbl_msg=Label(emp_frame,text=self.msg,font=("timesnew roman",20,'bold'),bg='white',fg='green',anchor='w')
        self.lbl_msg.place(x=100,y=290,relwidth=1)
         # Student Qr code
        qr_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_frame.place(x=600,y=100,width=250,height=380)
        
        qr_title=Label(qr_frame,text="Student Qr Code",font=("goudy old style",20),bg='#053746',fg='white').place(x=0,y=0,relwidth=1)
        self.qr_img=Label(qr_frame,text="No qr \n Available",relief=RIDGE,bg='blue',fg='white')
        self.qr_img.place(x=35,y=100,width=180,height=180)
        #=============to generate qr code=============
    def generate(self):
        
        if self.var_stu_roll.get()=='' or self.var_stu_name.get()==''or self.var_stu_class.get()==''or self.var_stu_sub.get()=='':
            self.msg="All Fields are required!!!"
            self.lbl_msg.config(text=self.msg,fg="red")
        else:
            qr_data=(F"Student Rollno:{self.var_stu_roll.get()}\n Student Name:{self.var_stu_name.get()}\n Student class:{self.var_stu_class.get()}\n Student subject:{self.var_stu_sub.get()}")
            qr_code=qrcode.make(qr_data)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("student qr code/Stu_"+str(self.var_stu_roll.get())+'.png')
            self.code_img=ImageTk.PhotoImage(file="student qr code/Stu_"+str(self.var_stu_roll.get())+'.png')
            self.qr_img.config(image=self.code_img)
            
            self.msg="Qr code generated!!!!"
            self.lbl_msg.config(text=self.msg,fg="green")
            #----------------------function to clear the date from the screen---------------------------
    def clear(self):
        self.var_stu_roll.set('')
        self.var_stu_name.set('')
        self.var_stu_class.set('')
        self.var_stu_sub.set('')
        self.qr_img.config(image='')
        self.msg=""
        self.lbl_msg.config(text=self.msg,fg="red")
        #-----------------------------------------------to save data in data base----------------------------------------
    def Submit(self):
        connection=m.connect(host="localhost",user="root",password="",database="manu")
        cur=connection.cursor() 
        query2=("insert into Student_Registration(stu_roll,stu_name,stu_class,stu_sub)values(' "+self.var_stu_roll.get()+" ',' "+self.var_stu_name.get()+" ',' "+self.var_stu_class.get()+" ',' "+self.var_stu_sub.get()+" ') ")
        cur.execute(query2)
        self.msg="Form Submitted!!!!!"
        self.lbl_msg.config(text=self.msg,fg="blue")
        #function to change the page of the tkinter
    def change(self):
        self.root.destroy()
        import page1
    
    

        
              


        
root=Tk()
obj=Qr_codegenerator(root)
root.mainloop()
