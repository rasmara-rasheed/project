
from tkinter import *
from tkinter import messagebox as mb
import sqlite3

with sqlite3.connect('myfirstapp.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEXT NOT NULL);')
db.commit()
db.close()

class main:
    def __init__(self,master):
    
        self.master = master

        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()

        self.widgets()


    def login(self):
        
        with sqlite3.connect('myfirstapp.db') as db:
            c = db.cursor()

        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            self.logw.pack_forget()
            self.mainw['text'] ="Welcome!\n\n"+self.username.get() 
            self.mainw['pady'] = 150
        else:
            mb.showerror('Error Occured!','INVALID USER CREDENTIALS.')
            
    def new_user(self):
        
        with sqlite3.connect('myfirstapp.db') as db:
            c = db.cursor()

       
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute('SELECT * FROM user WHERE username = ?',[(self.username.get())])        
        if c.fetchall():
            mb.showerror('Error!','Username already exists .')
        elif c.execute("SELECT * FROM user WHERE username = NULL"):
            mb.showerror('Error!','username cannot be blanked.')
        else:
            mb.showinfo('Success!','Account Created!')
            self.log()
        
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()



    def log(self):
        self.username.set('')
        self.password.set('')
        self.createw.pack_forget()
        self.mainw['text'] = 'LOGIN'
        self.logw.pack()
    
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logw.pack_forget()
        self.mainw['text'] = 'Create New Account'
        self.createw.pack()
        
    
    def widgets(self):
        self.mainw = Label(self.master,text = 'LOGIN',font = ('',50),pady =70,fg="red")
        self.mainw.pack()
        self.logw = Frame(self.master,padx =10,pady =70)
        Label(self.logw,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logw,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logw,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logw,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logw,text = ' Login ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login).grid()
        Button(self.logw,text = ' Create Account ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        self.logw.pack()
        
        self.createw = Frame(self.master,padx =10,pady = 10)
        Label(self.createw,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.createw,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.createw,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.createw,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.createw,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.new_user).grid(columnspan=2)
        #Button(self.createw,text = 'Go to Login',bd = 3 ,font = ('',15),padx=22,pady=5,command=self.log).grid(row=3,columnspan=2)

    

root = Tk()
root.title("My Login App")
main(root)
root.mainloop()