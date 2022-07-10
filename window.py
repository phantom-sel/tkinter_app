from tkinter import *
import sqlite3
import os

window = Tk()
window.geometry("1280x520")

# connect to database 
conn = sqlite3.connect('medicine.db')
# Create a cursor 
c = conn.cursor()
# # Query the database
try:
    c.execute("""CREATE TABLE medicines(
                med_name text,
                mfd char(11),
                exp char(11),
                stock integer
            )""")
except:
    print('database already exist!!')


''' ALL FUNCTIONS ARE HERE '''
def AddNewItem():

    AddNewWin = Tk()
    AddNewWin.geometry('470x400')
    # global window
    # window.destroy()
    # os.startfile('window.pyw')

    
    # c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'sa%' ")
    def submit():
        #for clear entry fields
        MedName.delete(0,END)
        Mfd.delete(0,END)
        ExpiryDate.delete(0,END)
        Stock.delete(0,END)
        # connect to database 
        conn = sqlite3.connect('medicine.db')
        # Create a cursor 
        c = conn.cursor()

        MedData = [(MedName.get(),Mfd.get(),ExpiryDate.get(),Stock.get())]
        c.executemany("INSERT INTO medicines VALUES (:MedName,:MFD,:ExpiryDate,:Stock),{''}")
        c.execute('SELECT *,OID FROM medicines')
        rec = c.fetchall()
        print(rec)

        conn.commit()
        conn.close()
    '''ENTRY FIELDS'''
    MedName = Entry(AddNewWin, width=30)
    MedName.grid(row=1,column=1,pady=10)
    Mfd = Entry(AddNewWin, width=30)
    Mfd.grid(row=2,column=1,pady=10)
    ExpiryDate = Entry(AddNewWin, width=30)
    ExpiryDate.grid(row=3,column=1,pady=10)
    Stock = Entry(AddNewWin, width=30)
    Stock.grid(row=4,column=1,pady=10)
    '''LABELS'''
    HeadlineLabel = Label(AddNewWin,text='Add New Items',font='Elephant 20 bold underline').grid(row=0,column=1,pady=10)
    MedNameLabel = Label(AddNewWin,text='Medicine Name:',font='CooperBlack 15 ').grid(row=1,column=0,pady=10)
    MFDLabel = Label(AddNewWin,text='Manufacturing Date:',font='CooperBlack 15 ').grid(row=2,column=0,pady=10)
    ExpiryDateLabel = Label(AddNewWin,text='Expiry Date:',font='CooperBlack 15 ').grid(row=3,column=0,pady=10)
    StockLabel = Label(AddNewWin,text='Stock(strp):',font='CooperBlack 15 ').grid(row=4,column=0,pady=10)
    '''BUTTONS'''
    SubmitButton = Button(AddNewWin,text='Submit',width=60,bg='black',fg='white',command=submit).grid(row=5,column=0,columnspan=10,padx=20,pady=10)

    

def NearExpiry():
    pass

def Refresh():
    pass

def ComingSoon():
    pass

''' this code script is auto genrated '''

#\\ for gui shape and main bg colour \\
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

#\\ for background image... \\
background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    640.0, 360.0,
    image=background_img)

#\\ for main headline... \\
canvas.create_text(
    662.5, 73.0,
    text = "Generic Medicine Management System ",
    fill = "#000000",
    font = ("Inter-Black", int(40.0)))

#\\ for near expiry button \\
img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = NearExpiry,
    relief = "flat")
b0.place(
    x = 514, y = 132,
    width = 258,
    height = 246)

#\\ for Unknown or Coming soon.. button \\
img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = ComingSoon,
    relief = "flat")
b1.place(
    x = 974, y = 132,
    width = 258,
    height = 246)

#\\ for add new item button \\
img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = AddNewItem,
    relief = "flat")
b2.place(
    x = 54, y = 132,
    width = 258,
    height = 246)

#\\ for text called numbers.. it's a temproray label \\
canvas.create_text(
    614.0, 540.5,
    text = "Numbers...",
    fill = "#000000",
    font = ("Inter-Black", int(40.0)))

#\\ for text called expired items and it's a fixed label \\
canvas.create_text(
    276.5, 457.5,
    text = "expired items",
    fill = "#000000",
    font = ("Inter-Black", int(40.0)))

#\\ for button who Refresh items on bottom lists \\
img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = Refresh,
    relief = "flat")
b3.place(
    x = 426, y = 620,
    width = 367,
    height = 84)

# window.resizable(False, False)

conn.commit() #take a photo
conn.close()  #close the connection

window.mainloop()
