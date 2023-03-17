from tkinter import *
from tkinter.ttk import *
import sqlite3
from datetime import datetime

conn = sqlite3.connect('tasks.sqlite')
cur = conn.cursor()
cats =[]

def error(err):
    root = Tk()
    root.title('Error')
    root.iconbitmap('icon.ico')
    Label(root,text="you can't perform this action\n"+str(err)).pack(padx=10,pady=10)
cur.executescript('''
    CREATE TABLE IF NOT EXISTS category(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE NOT NULL
    );
    CREATE TABLE IF NOT EXISTS tasks(
    cat_id INTEGER
    title TEXT
    descript TEXT
    Due DATE
    )
''')


def new_c():
    root1 =Tk()
    root1.title('new category')
    root1.iconbitmap('icon.ico')
    root1.geometry('300x100')
    Label(root1,text='name').grid(padx=10,pady=10)
    name = Entry(root1)
    name.grid(column=5,row=0,padx=10,pady=10)
    b = lambda : root1.destroy()
    def category(name):
        global cur
        global conn
        try:
            cur.execute('''INSERT INTO category(name) VALUES( ? )''',(name,))
            conn.commit()
            cur.execute('''SELECT id FROM category WHERE name = ?''',(name,))
            b()
            e(name,cur.fetchone()[0])
        except Exception as z:
            error(z)
    a = lambda :category(name.get())
    d = Button(root1,text='Create category',command=a)
    d.grid(column=10,row=0,padx=10,pady=10)

root= Tk()
root.title('My tasks')
root.iconbitmap('icon.ico')
root.geometry('300x300')
new_buttons = Frame(root)
new_buttons.pack(fill='both',side='top')
new_cat = Button(new_buttons,text='New category',command=new_c)
new_cat.pack(anchor='w',padx=10,pady=10)
note = Notebook(root)
note.pack(padx=10,pady=10,fill ='both',expand = 1)
class task():
    def __init__(self,cat,name,deadline,descript):
        self.cat = cat
        self.name = name
        self.deadline = deadline
        self.descript= descript
        self.fram = Frame(self.cat.frm)
        self.fram.pack()
        Button(self.fram).pack()
class category():
    global note
    def __init__(self,name,id):
        def ntask():
            root1 =Tk()
            root1.title('new Task')
            root1.iconbitmap('icon.ico')
            Label(root1,text='name').grid(padx=10,pady=10)
            name = Entry(root1)
            name.grid(column=1,row=0,padx=10,pady=10)
            Label(root1,text='Due Time').grid(padx=10,pady=10,row=1)
            dt = Entry(root1)
            dt.grid(column=1,row=1,padx=10,pady=10)
            Label(root1,text='Due date').grid(padx=10,pady=10,row=2)
            dd = Entry(root1)
            dd.grid(column=1,row=2,padx=10,pady=10)
            desc = Text(root1,height=10,width=30,relief='solid')
            desc.grid(row=3,padx=10,pady=10,columnspan=2)
            Button(root1,text='Create task',command= lambda :task(self,name.get(),dd.get(),desc.get('1.0','end'))).grid(row=4,padx=10,pady=10,columnspan=2)
        global note
        self.name = name
        self.id = id
        self.frm = Frame(note)
        note.add(self.frm,text=self.name)
        self.buts = Frame(self.frm)
        self.buts.pack(fill='both',side='top')
        self.nt = Button(self.buts,text='new task',command= ntask)
        self.nt.grid(padx=10,pady=10)
        self.de = Button(self.buts,text='category details',command=self.details)
        self.de.grid(padx=10,pady=10,column=2,row=0)

    def Delete(self):
        try:
            cur.execute('''DELETE FROM category WHERE name = ? ''',(self.name,))
            cur.execute('''DELETE FROM tasks WHERE cat_id = ?''',(self.id,))
            conn.commit()
        except Exception as e:
            error(e)
        note.forget(self.tabid)
        self.root2.destroy()
        del self
    def details(self):
        self.tabid = note.index(note.select())
        def update(n):
            global cur
            note.tab(self.tabid,text=n)
            try:
                cur.execute('''UPDATE category SET name = ? WHERE name = ?''',(n,self.name))
                conn.commit()
                self.name = n
                self.root2.destroy()
            except Exception as e:
                error(e)
        self.root2 =Tk()
        self.root2.title('category details - '+self.name)
        self.root2.iconbitmap('icon.ico')
        Label(self.root2,text='Name').grid(padx=10,pady=10)
        name = Entry(self.root2)
        name.insert(END,self.name)
        name.grid(padx=10,pady=10,row=0,column=1)
        Button(self.root2,text='Apply',command = lambda : update(name.get())).grid(row=1,column=0,padx=10,pady=10)
        Button(self.root2,text='Delete category',command = lambda : self.Delete()).grid(row=1,column=1,padx=10,pady=10)
        Button(self.root2,text='Cancel',command= lambda: self.root2.destroy()).grid(row=1,column=2,padx=10,pady=10)

e = lambda g,h : category(g,h)
cur.execute('''SELECT name,id FROM category''')

for i in cur.fetchall():
    category(i[0],i[1])

mainloop()
