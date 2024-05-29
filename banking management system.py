# imports
from tkinter import *
import os
from PIL import ImageTk, Image

# Main Screen
master = Tk()
master.title("Banking App")
master.geometry("400x300")



def set_image():
    global bck_end_2
    image_2 = Image.open('bank_1.jpg')
    bck_end_2 = ImageTk.PhotoImage(image_2.resize((390, 290)))
    lbl = Label(master, image=bck_end_2)
    lbl.place(x=0, y=0)
set_image()
Frame(master, width=250, height=190, bg='#CCE5FF').place(x=80, y=100)

# Functions
def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    contact_no = temp_contact_no.get()
    address = temp_address.get()
    city= temp_state.get()
    state = temp_state.get()
    password = temp_password.get()
    all_accounts = os.listdir()

    if name == "" or age == "" or gender == "" or contact_no == "" or address == "" or city == "" or state == "" or password == "":
        notif.config(fg="red", text="All fields required * ")
        return

    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red", text="Account already exists")
            return
        else:
            new_file = open(name, "w")
            new_file.write(name + '\n')
            new_file.write(password + '\n')
            new_file.write(age + '\n')
            new_file.write(contact_no + '\n')
            new_file.write(address + '\n')
            new_file.write(city + '\n')
            new_file.write(state + '\n')
            new_file.write(gender + '\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg="green", text="Account has been created")


def register():
    # Vars
    global temp_name
    global temp_age
    global temp_gender
    global temp_contact_no
    global temp_address
    global temp_city
    global temp_state
    global temp_password
    global notif
    global bck_end_1
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_contact_no = StringVar()
    temp_address = StringVar()
    temp_city = StringVar()
    temp_state = StringVar()
    temp_password = StringVar()

    # Register Screen
    register_screen = Toplevel(master)
    register_screen.title('Register')
    register_screen.geometry("700x700")
    image_1 = Image.open('bank_1.jpg')
    bck_end_1 = ImageTk.PhotoImage(image_1.resize((690,690)))
    lbl = Label(register_screen, image=bck_end_1)
    lbl.place(x=0, y=0)
    Frame(register_screen, width=450, height=460, bg='#CCE5FF').place(x=120, y=230)
    

    # Labels
    Label(register_screen, text="Please enter your details below to register",  bg='#CCE5FF',font=('Calibri', 17)).place(x=130,y=230)
    Label(register_screen, text="Name", bg='#CCE5FF', font=('Calibri', 15)).place(x=120,y=280)
    Label(register_screen, text="Age",  bg='#CCE5FF',font=('Calibri', 15)).place(x=120,y=320)
    Label(register_screen, text="Gender", bg='#CCE5FF', font=('Calibri', 15)).place(x=120,y=360)
    Label(register_screen, text="Contact NO",  bg='#CCE5FF',font=('Calibri', 15)).place(x=120,y=400)
    Label(register_screen, text="Address", bg='#CCE5FF',font=('Calibri', 15)).place(x=120,y=440)
    Label(register_screen, text="City",bg='#CCE5FF', font=('Calibri', 15)).place(x=120,y=480)
    Label(register_screen, text="State",bg='#CCE5FF', font=('Calibri', 15)).place(x=120,y=520)
    Label(register_screen, text="Password",bg='#CCE5FF', font=('Calibri', 15)).place(x=120,y=560)
    notif = Label(register_screen,bg='#CCE5FF', font=('Calibri', 12))
    notif.place(x=200,y=660)
    # Entries
    Entry(register_screen, textvariable=temp_name,width=28).place(x=260,y=280)
    Entry(register_screen, textvariable=temp_age,width=28).place(x=260,y=320)
    Entry(register_screen, textvariable=temp_gender,width=28).place(x=260,y=360)
    Entry(register_screen, textvariable=temp_contact_no,width=28).place(x=260,y=400)
    Entry(register_screen, textvariable=temp_address,width=28).place(x=260,y=440)
    Entry(register_screen, textvariable=temp_city,width=28).place(x=260,y=480)
    Entry(register_screen, textvariable=temp_state,width=28).place(x=260,y=520)
    Entry(register_screen, textvariable=temp_password,width=28, show="*").place(x=260,y=560)
    # Buttons
    Button(register_screen, text="Register",width=20, command=finish_reg, font=('Calibri', 12)).place(x=200,y=620)
    
def login_session():
    global login_name
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    for name in all_accounts:
        if name == login_name:
            file = open(name, "r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[1]
            # Account Dashboard
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title('Dashboard')
                account_dashboard.geometry("300x300")
                Frame(account_dashboard, width=300, height=300, bg='#CCE5FF').place(x=0, y=0)
                # Labels
                Label(account_dashboard,bg='#CCE5FF', text="Account Dashboard", font=('Calibri', 12)).grid(row=0, stick=N, pady=10)
                Label(account_dashboard, bg='#CCE5FF',text="Welcome " + name, font=('Calibri', 12)).grid(row=1, sticky=N, pady=5)
                # Buttons
                Button(account_dashboard, text="Personal Details", font=('Calibri', 12), width=30,
                       command=personal_details).grid(row=2, sticky=N, padx=10)
                Button(account_dashboard, text="Deposit", font=('Calibri', 12), width=30, command=deposit).grid(row=3,
                                                                                                                sticky=N,
                                                                                                                padx=10)
                Button(account_dashboard, text="Withdraw", font=('Calibri', 12), width=30, command=withdraw).grid(row=4,
                                                                                                                  sticky=N,
                                                                                                                  padx=10)
                Label(account_dashboard,bg='#CCE5FF',).grid(row=5, sticky=N, pady=10)
                return
            else:
                login_notif.config(fg="red",bg='#CCE5FF', text="Password Incorrect!!")
                return
    login_notif.config(fg="red",bg='#CCE5FF', text="No Account Found!!")


def deposit():
    # Vars
    global amount
    global deposit_notif
    global current_balance_label
    amount = StringVar()
    file = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[8]
    # Deposit Screen
    deposit_screen = Toplevel(master)
    deposit_screen.title('Deposit')
    deposit_screen.geometry("320x180")
    Frame(deposit_screen, width=320, height=190, bg='#CCE5FF').place(x=0, y=0)
    # Label
    Label(deposit_screen, text="Deposit",bg='#CCE5FF', font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    current_balance_label = Label(deposit_screen,bg='#CCE5FF',text="Current Balance : Rs " + details_balance, font=('Calibri', 12))
    current_balance_label.grid(row=1, sticky=W)
    Label(deposit_screen, text="Amount : ",bg='#CCE5FF', font=('Calibri', 12)).grid(row=2, sticky=W)
    deposit_notif = Label(deposit_screen,bg='#CCE5FF', font=('Calibri', 12))
    deposit_notif.grid(row=4, sticky=N, pady=5)
    # Entry
    Entry(deposit_screen, textvariable=amount).grid(row=2, column=1)
    # Button
    Button(deposit_screen, text="Finish", font=('Calibri', 12), command=finish_deposit).grid(row=3, sticky=N, pady=5)


def finish_deposit():
    if amount.get() == "":
        deposit_notif.config(text='Amount is required', fg="red")
    if float(amount.get()) <= 0:
        deposit_notif.config(text='Negative currency is not accepted', fg='red')
        return

    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[8]
    updated_balance = current_balance
    updated_balance = float(updated_balance) + float(amount.get())
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance : Rs" + str(updated_balance), fg="green")
    deposit_notif.config(text='Balance Updated', fg='green')


def withdraw():
    # Vars
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount = StringVar()
    file = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[8]
    # withdraw Screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title('Withdraw')
    withdraw_screen.geometry("320x180")
    Frame(withdraw_screen,width=320, height=180,   bg='#CCE5FF').place(x=0, y=0)
    # Label
    Label(withdraw_screen, text="Withdraw",  bg='#CCE5FF',font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    current_balance_label = Label(withdraw_screen, text="Current Balance : Rs" + details_balance,  bg='#CCE5FF',font=('Calibri', 12))
    current_balance_label.grid(row=1, sticky=W)
    Label(withdraw_screen, text="Amount : ",  bg='#CCE5FF', font=('Calibri', 12)).grid(row=2, sticky=W)
    withdraw_notif = Label(withdraw_screen, font=('Calibri', 12),bg='#CCE5FF')
    withdraw_notif.grid(row=4, sticky=N, pady=5)
    # Entry
    Entry(withdraw_screen, textvariable=withdraw_amount).grid(row=2, column=1)
    # Button
    Button(withdraw_screen, text="Finish", font=('Calibri', 12), bg= '#ffffff', command=finish_withdraw).grid(row=3, sticky=N, pady=5)


def finish_withdraw():
    if withdraw_amount.get() == "":
        withdraw_notif.config(text='Amount is required', fg="red", bg='#CCE5FF')
    if float(withdraw_amount.get()) <= 0:
        withdraw_notif.config(text='Negative currency is not accepted', fg='red', bg='#CCE5FF')
        return

    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[8]

    if float(withdraw_amount.get()) > float(current_balance):
        withdraw_notif.config(text='Insufficient Funds!!', fg='red', bg='#CCE5FF')
        return
    updated_balance = current_balance
    updated_balance = float(updated_balance) - float(withdraw_amount.get())
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance : Rs" + str(updated_balance), fg="green", bg='#CCE5FF')
    withdraw_notif.config(text='Balance Updated', fg='green', bg='#CCE5FF')


def personal_details():
    # Vars
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_name = user_details[0]
    details_age = user_details[2]
    details_gender = user_details[7]
    details_contact_no = user_details[3]
    details_address = user_details[4]
    details_city = user_details[5]
    details_state = user_details[6]
    details_balance = user_details[8]
    
    # Personal details screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Personal Details')
    personal_details_screen.geometry("300x350")
    Frame(personal_details_screen, width=300, height=350, bg='#CCE5FF').place(x=0, y=0)
    # Labels
    Label(personal_details_screen, text="Personal Details",bg='#CCE5FF', font=('Calibri', 17)).grid(row=0, sticky=N, pady=10)
    Label(personal_details_screen, text="Name : " + details_name,bg='#CCE5FF', font=('Calibri', 15)).grid(row=1, sticky=W)
    Label(personal_details_screen, text="Age : " + details_age,bg='#CCE5FF',  font=('Calibri', 15)).grid(row=2, sticky=W)
    Label(personal_details_screen, text="Gender : " + details_gender,bg='#CCE5FF',  font=('Calibri', 15)).grid(row=3, sticky=W)
    Label(personal_details_screen, text="Contact No: " + details_contact_no,bg='#CCE5FF',font=('Calibri', 15)).grid(row=4, sticky=W)
    Label(personal_details_screen, text="Address : " + details_address,bg='#CCE5FF',  font=('Calibri', 15)).grid(row=5, sticky=W)
    Label(personal_details_screen, text="City : " + details_city,bg='#CCE5FF',  font=('Calibri', 15)).grid(row=6, sticky=W)
    Label(personal_details_screen, text="State : " + details_state,bg='#CCE5FF',  font=('Calibri', 15)).grid(row=7, sticky=W)
    Label(personal_details_screen, text="Balance :Rs " + details_balance,bg='#CCE5FF',  font=('Calibri', 15)).grid(row=9, sticky=W)


def login():
    # Vars
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    global bck_end
    temp_login_name = StringVar()
    temp_login_password = StringVar()
    # Login Screen
    login_screen = Toplevel(master)

    login_screen.title('Login')
    login_screen.geometry("700x700")

    image_0 = Image.open('bank.jpg')
    bck_end = ImageTk.PhotoImage(image_0.resize((690,690)))
    lbl = Label(login_screen, image=bck_end)
    lbl.place(x=0, y=0)

    Frame(login_screen, width=400, height=460, bg='#CCE5FF').place(x=240, y=230)

    # Labels
    Label(login_screen, text="Login to your account",bg='#CCE5FF', font=('Calibri', 26,'bold')).place(x=260, y=230)
    Label(login_screen, text="Username",bg='#CCE5FF',font=('Harrinton',22,"bold",'italic')).place(x=240,y=330)
    Label(login_screen, text="Password",bg='#CCE5FF', font=('Harrinton',22,"bold",'italic')).place(x=240,y=430)
    login_notif = Label(login_screen,bg='#CCE5FF', font=('Calibri', 12))
    login_notif.place(x=330,y=500)
    # Entry
    Entry(login_screen, textvariable=temp_login_name,width=14 ,font=('Harrinton',20,"bold",'italic')).place(x=400,y=330)
    Entry(login_screen, textvariable=temp_login_password, show="*",width=14 ,font=('Harrinton',20,"bold",'italic')).place(x=400,y=430)
    # Buttons
    Button(login_screen, text="Login", command=login_session, width=10, font=('Harrinton',20,"bold",'italic')).place(x=330,y=530)


# Labels
Label(master, text="SKY BANK",bg='#CCE5FF', font=('Calibri', 14)).place(x=150,y=120)
Label(master, text="The most secure bank you've probably used EVER",bg='#CCE5FF', font=('calibri', 12)).place(x=40,y=160)


# Buttons
Button(master, text="Register", font=('Calibri', 12), width=20, command=register).place(x=100,y=200)
Button(master, text="Login",font=('Calibri', 12), width=20, command=login).place(x=100,y=240)

master.mainloop()

