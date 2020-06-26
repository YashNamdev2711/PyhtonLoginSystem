from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
t=Tk()
t.minsize(425,350)
f55=None
def login():
    f2=Frame(bg="#091e42")      
    f2.place(x=0,y=0,width=425,height=350)
    s1=StringVar()
    s2=StringVar()
    
    
    u=Label(f2,text="LogIn Page",bg="#091e42",fg="white")
    u.place(x=150,y=10)
    
    u1=Label(f2,text="enter name",bg="#091e42",fg="white")
    u1.place(x=100,y=80)
    e1=Entry(f2,font=("",12),textvariable=s1)
    e1.place(x=200,y=80,width=120)
    
    u2=Label(f2,text="enter pass",bg="#091e42",fg="white")
    u2.place(x=100,y=130)
    e2=Entry(f2,font=("",12),show='*',textvariable=s2)
    e2.place(x=200,y=130,width=120)
    
    def login1():
            db=sqlite3.connect('abhi.db')
            cr=db.cursor()
            r=cr.execute("select * from regis where UNAME='"+s1.get()+"' AND UPASS='"+s2.get()+"'")
            for r1 in r:
                    mymenu()
                    #messagebox.showinfo("HEY","Welcome")
                    break
            else:
                messagebox.showinfo("OOPS :-(","Invalid Username and Password")
              
            db.commit()
            db.close()
            s1.set("")
            s2.set("")
            
    
    
    b3=Button(f2,text="LogIn",command=login1,bg="#091e42",fg="white")
    b3.place(x=150,y=200,width=60,height=40)
    
    b2=Button(f2,text="Home",command=home,bg="#091e42",fg="white")
    b2.place(x=15,y=300,width=60,height=40)
    
    b4=Button(f2,text="regis",command=regis,bg="#091e42",fg="white")
    b4.place(x=350,y=300,width=60,height=40)
def regis():
    f3=Frame(bg="#091e42")
    f3.place(x=0,y=0,width=425,height=350)
    r1=StringVar()
    r2=StringVar()
    r3=StringVar()
    u=Label(f3,text="registration page",bg="#091e42",fg="white")
    u.place(x=150,y=10)
    
    u1=Label(f3,text="enter name",bg="#091e42",fg="white")
    u1.place(x=100,y=80)
    e1=Entry(f3,font=("",12),textvariable=r1)
    e1.place(x=200,y=80,width=120)
    
    u2=Label(f3,text="enter pass",bg="#091e42",fg="white")
    u2.place(x=100,y=130)
    e2=Entry(f3,font=("",12),show='*',textvariable=r2)
    e2.place(x=200,y=130,width=120)
    
    u3=Label(f3,text="C number",bg="#091e42",fg="white")
    u3.place(x=100,y=180)
    e3=Entry(f3,font=("",12),textvariable=r3)
    e3.place(x=200,y=180,width=120)
    def regis1():
            db=sqlite3.connect('abhi.db')
            cr=db.cursor()
            cr.execute("insert into regis values('"+r1.get()+"','"+r2.get()+"','"+r3.get()+"')")
            db.commit()
            db.close()
            messagebox.showinfo("CONGRATULATION","You Are Registerd")
            r1.set("")
            r2.set("")
            r3.set("")
    
    b3=Button(f3,text="register",command=regis1,bg="#091e42",fg="white")
    b3.place(x=150,y=250,width=60,height=40)
    
    b2=Button(f3,text="Home",command=home,bg="#091e42",fg="white")
    b2.place(x=15,y=300,width=60,height=40)
    b5=Button(f3,text="Login",command=login,bg="#091e42",fg="white")
    b5.place(x=350,y=300,width=60,height=40)
    
def mymenu():
        n=ttk.Notebook()
        n.place(x=0,y=0,width=600,height=400)
        def demo(a):
                if(n.index("current")==5):
                        home()
        n.bind("<<NotebookTabChanged>>",demo)
        insertdata(n)
        showalldata(n)
        Searchdata(n)
        Updatedata(n)
        Deletdata(n)
        Logout(n)

def insertdata(n):
        f4=Frame(bg="#091e42")
        n.add(f4,text="Insert")
        s1=StringVar()
        s2=StringVar()
        s3=StringVar()
        s4=StringVar()
        s5=StringVar()
   
        
        u1=Label(f4,text="enter RNO",bg="#091e42",fg="white")
        u1.place(x=100,y=60)
        e1=Entry(f4,font=("",12),textvariable=s1)
        e1.place(x=200,y=60,width=120)
        
        u2=Label(f4,text="enter name",bg="#091e42",fg="white")
        u2.place(x=100,y=90)
        e2=Entry(f4,font=("",12),textvariable=s2)
        e2.place(x=200,y=90,width=120)
        
        u3=Label(f4,text="enter Phy",bg="#091e42",fg="white")
        u3.place(x=100,y=120)
        e3=Entry(f4,font=("",12),textvariable=s3)
        e3.place(x=200,y=120,width=120)
        
        u4=Label(f4,text="enter Che",bg="#091e42",fg="white")
        u4.place(x=100,y=150)
        e4=Entry(f4,font=("",12),textvariable=s4)
        e4.place(x=200,y=150,width=120)
        
        u5=Label(f4,text="enter Maths",bg="#091e42",fg="white")
        u5.place(x=100,y=180)
        e5=Entry(f4,font=("",12),textvariable=s5)
        e5.place(x=200,y=180,width=120)
        
        def insertdemo1():
            db=sqlite3.connect('abhi.db')
            cr=db.cursor()
            cr.execute("insert into ins values('"+s1.get()+"','"+s2.get()+"','"+s3.get()+"','"+s4.get()+"','"+s5.get()+"')")
            db.commit()
            db.close()
            messagebox.showinfo("okay","Insert Data")
            s1.set("")
            s2.set("")
            s3.set("")
            s4.set("")
            s5.set("")
            showalldata1(f55)
        b1=Button(text="Insert",command=insertdemo1)
        b1.place(x=200,y=250,width=80,height=20)

def showalldata(n):
        f5=Frame(bg="#091e42")
        n.add(f5,text="ShowAll")
        global f55
        f55=f5
        showalldata1(f5)
def showalldata1(f5):
        for w in f5.winfo_children():
                    w.destroy()
        u1=Label(f5,text="RNO",bg="#091e42",fg="white")
        u1.place(x=0,y=0)
        u2=Label(f5,text="Name",bg="#091e42",fg="white")
        u2.place(x=90,y=0)
        u3=Label(f5,text="Phy",bg="#091e42",fg="white")
        u3.place(x=180,y=0)
        u4=Label(f5,text="che",bg="#091e42",fg="white")
        u4.place(x=270,y=0)
        u5=Label(f5,text="Maths",bg="#091e42",fg="white")
        u5.place(x=360,y=0)
        db=sqlite3.connect('abhi.db')
        cr=db.cursor()
        r=cr.execute("select * from ins")
        x=0
        y=60
        for r1 in r:
                Label(f5,text=r1[0],bg="#091e42",fg="white").place(x=x,y=y)
                x+=90
                Label(f5,text=r1[1],bg="#091e42",fg="white").place(x=x,y=y)
                x+=90
                Label(f5,text=r1[2],bg="#091e42",fg="white").place(x=x,y=y)
                x+=90
                Label(f5,text=r1[3],bg="#091e42",fg="white").place(x=x,y=y)
                x+=90
                Label(f5,text=r1[4],bg="#091e42",fg="white").place(x=x,y=y)
                y+=40
                x=0
        db.commit()
        db.close()

def Searchdata(n):
        f6=Frame(bg="#091e42")
        n.add(f6,text="SearchData")
        s1=StringVar()
        
        u1=Label(f6,text="enter Rno",bg="#091e42",fg="white")
        u1.place(x=100,y=80)
        e1=Entry(f6,font=("",12),textvariable=s1)
        e1.place(x=200,y=80,width=120)
        def searchdata1():
            db=sqlite3.connect('abhi.db')
            cr=db.cursor()
            r=cr.execute("select * from ins where URNO='"+s1.get()+"'")
            for r1 in r:
                    u3=Label(f6,text="Name is",bg="#091e42",fg="white")
                    u3.place(x=100,y=120)
                    u4=Label(f6,text=r1[1],bg="#091e42",fg="white")
                    u4.place(x=200,y=120)
                    u5=Label(f6,text="phy",bg="#091e42",fg="white")
                    u5.place(x=100,y=150)
                    u6=Label(f6,text=r1[2],bg="#091e42",fg="white")
                    u6.place(x=200,y=150)
                    u7=Label(f6,text="che",bg="#091e42",fg="white")
                    u7.place(x=100,y=180)
                    u8=Label(f6,text=r1[3],bg="#091e42",fg="white")
                    u8.place(x=200,y=180)
                    u9=Label(f6,text="Maths",bg="#091e42",fg="white")
                    u9.place(x=100,y=210)
                    u10=Label(f6,text=r1[4],bg="#091e42",fg="white")
                    u10.place(x=200,y=210,)
                    break
            else:
                messagebox.showinfo("soory","Invalid roll no")
                u14=Label(f6,text="",bg="#091e42",fg="white")
                u14.place(x=100,y=120,width=300) 
                u15=Label(f6,text="",bg="#091e42",fg="white")
                u15.place(x=100,y=150,width=300) 
                u16=Label(f6,text="",bg="#091e42",fg="white")
                u16.place(x=100,y=180,width=300)
                u14=Label(f6,text="",bg="#091e42",fg="white")
                u14.place(x=100,y=210,width=300)                
                                
            db.commit()
            db.close()
        
        b1=Button(f6,text="Search!!",bg="#091e42",fg="white",command=searchdata1)
        b1.place(x=350,y=80,height=20)
        
        
       
def Updatedata(n):
        f7=Frame(bg="#091e42")
        n.add(f7,text="UpdateALL")
        s1=StringVar()
        u1=Label(f7,text="enter Rno",bg="#091e42",fg="white")
        u1.place(x=100,y=80)
        e1=Entry(f7,font=("",12),textvariable=s1)
        e1.place(x=200,y=80,width=120)
        def Updatedata1():
            db=sqlite3.connect('abhi.db')
            cr=db.cursor()
            r=cr.execute("select * from ins where URNO='"+s1.get()+"'")
            for r1 in r:
                    s2=StringVar()
                    s3=StringVar()
                    s4=StringVar()
                    s5=StringVar()
                    u3=Label(f7,text="Name is",bg="#091e42",fg="white")
                    u3.place(x=100,y=120)
                    u4=Entry(f7,bg="#091e42",fg="white",textvariable=s2)
                    u4.insert(0,r1[1])
                    u4.place(x=200,y=120)
                    u5=Label(f7,text="phy is",bg="#091e42",fg="white")
                    u5.place(x=100,y=150)
                    u6=Entry(f7,bg="#091e42",fg="white",textvariable=s3)
                    u6.insert(0,r1[2])
                    u6.place(x=200,y=150)
                    u7=Label(f7,text="che is",bg="#091e42",fg="white")
                    u7.place(x=100,y=180)
                    u8=Entry(f7,bg="#091e42",fg="white",textvariable=s4)
                    u8.insert(0,r1[3])
                    u8.place(x=200,y=180)
                    u9=Label(f7,text="math is",bg="#091e42",fg="white")
                    u9.place(x=100,y=210)
                    u10=Entry(f7,bg="#091e42",fg="white",textvariable=s5)
                    u10.insert(0,r1[4])
                    u10.place(x=200,y=210)
                    def Updatedata2():
                                db=sqlite3.connect('abhi.db')
                                cr=db.cursor()
                                cr.execute("update ins set UNAME='"+s2.get()+"',UPHY='"+s3.get()+"',UCHE='"+s4.get()+"',UMATHS='"+s5.get()+"' where URNO='"+s1.get()+"'")
                                db.commit()
                                db.close()
                                showalldata1(f55)
                                messagebox.showinfo("CONGRATULATION","Data Updated")
                               
                    b11=Button(f7,text="Update",bg="#091e42",fg="white",command=Updatedata2)
                    b11.place(x=300,y=300,height=20)
                    
                    break
            else:
                messagebox.showinfo("soory","Invalid roll no")
                u14=Label(f7,text="",bg="#091e42",fg="white")
                u14.place(x=100,y=120,width=300) 
                u15=Label(f7,text="",bg="#091e42",fg="white")
                u15.place(x=100,y=150,width=300) 
                u16=Label(f7,text="",bg="#091e42",fg="white")
                u16.place(x=100,y=180,width=300)
                u14=Label(f7,text="",bg="#091e42",fg="white")
                u14.place(x=100,y=210,width=300)                
                                
            db.commit()
            db.close()
        
        b1=Button(f7,text="Update!!",bg="#091e42",fg="white",command= Updatedata1)
        b1.place(x=350,y=80,height=20)
       
        
def Deletdata(n):
        f8=Frame(bg="#091e42")
        n.add(f8,text="Delet")
        d1=StringVar()
        u1=Label(f8,text="enter Rno",bg="#091e42",fg="white")
        u1.place(x=100,y=80)
        
        e1=Entry(f8,font=("",12),textvariable=d1)
        e1.place(x=200,y=80,width=120)
        def deletdata1():
                    db=sqlite3.connect('abhi.db')
                    cr=db.cursor()
                    cr.execute("delete from ins where URNO='"+d1.get()+"'")
                    db.commit()
                    db.close()
                    showalldata1(f55)
                    messagebox.showinfo("okay","Data deleted")
                    d1.set("")
        b1=Button(f8,text="Delet!",bg="#091e42",fg="white",command=deletdata1)
        b1.place(x=320,y=80,width=100)

def Logout(n):
        f9=Frame(bg="#091e42")
        n.add(f9,text="logout")



def home():
    f1=Frame(bg="#091e42")
    f1.place(x=0,y=0,width=425,height=350)
    b1=Button(f1,text="login!!",command=login,bg="#091e42",fg="white")
    b1.place(x=100,y=50,width=80,height=40)
    b2=Button(f1,text="Regis",command=regis,bg="#091e42",fg="white")
    b2.place(x=200,y=50,width=80,height=40)
home()
t.mainloop()