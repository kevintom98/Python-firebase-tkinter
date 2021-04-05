from tkinter import *
import pyrebase


firebaseConfig ={'apiKey': "AIzaSyDDOUUPzA2OuTT9deZcHCtBe88C3JmHUOI",
    'authDomain': "aisa-4b073.firebaseapp.com",
    'databaseURL': "https://aisa-4b073-default-rtdb.firebaseio.com",
    'projectId': "aisa-4b073",
    'storageBucket': "aisa-4b073.appspot.com",
    'messagingSenderId': "714681750998",
    'appId': "1:714681750998:web:9b195c244d9fd2b64a4077",
    'measurementId': "G-E7WH5S8B7P"}

firebase = pyrebase.initialize_app(firebaseConfig)




def register_user():
    auth = firebase.auth()
    db= firebase.database()

    username_info = username.get()
    password_info = password.get()

    name1 = name.get()
    vehicle_no1 = vehicle_no.get()
    rc_book_no1= rc_book_no.get()
    dl_no1= dl_no.get()

    try:
        user = auth.create_user_with_email_and_password(username_info,password_info)
        msg = Message(screen1, text = "Registration sucessfull!")  
        msg.pack()
        print("Registration Sucessfull")
        
        data = {'name': name1, 'vehicle_no': vehicle_no1, 'RC_Book_no': rc_book_no1, 'DL_no': dl_no1}
        db.child('Users').child(vehicle_no1).set(data)
        
        screen1.destroy()
    
    except:
        msg = Message(screen1, text = "Registration Unsucessfull!")  
        msg.pack()







def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title ("Register")
    screen1.geometry ("300x250")

    global username,password,name,vehicle_no,rc_book_no,dl_no

    username = StringVar()
    password = StringVar()
    name =  StringVar()
    vehicle_no = StringVar()
    rc_book_no = StringVar()
    dl_no = StringVar()

    Label(text="").pack()
    Label(screen1,text="Name").pack()
    Entry(screen1,textvariable = name).pack()
    Label(screen1,text="Vehicle Number").pack()
    Entry(screen1,textvariable = vehicle_no).pack()
    Label(screen1,text="RC Book Number").pack()
    Entry(screen1,textvariable = rc_book_no).pack()
    Label(screen1,text="Driving License Number").pack()
    Entry(screen1,textvariable = dl_no).pack()
    Label(screen1,text="Username").pack()
    Entry(screen1,textvariable = username).pack()
    Label(screen1,text="Password").pack()
    Entry(screen1,textvariable = password,show='*').pack()
    Label(text="").pack()
    Button(screen1, text = "Register", width =10, height = 1, command = register_user).pack()






def login_user():
    auth = firebase.auth()

    username = login_username.get()
    password = login_password.get()

    try:
        login = auth.sign_in_with_email_and_password(username, password)
        msg = Message(screen2, text = "Login sucessfull!")  
        msg.pack()
        print("Login Sucessfull")
        screen2.destroy()
    except:
        msg = Message(screen2, text = "Wrong Username/Password")  
        msg.pack()






def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title ("Login")
    screen2.geometry ("300x250")
    
    global login_username, login_password

    login_username = StringVar()
    login_password = StringVar()

    Label(screen2,text="AISA", bg="grey", width = '300', height = '2', font=("Calibri", 13)).pack()
    Label(screen2,text="").pack()
    Label(screen2,text="Username").pack()
    Entry(screen2,textvariable = login_username).pack()
    Label(screen2,text="Password").pack()
    Entry(screen2,textvariable = login_password,show='*').pack()
    Label(text="").pack()
    Button(screen2, text = "Login", width =10, height = 1, command = login_user).pack()






def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("A.I.S.A")
    Label(text="AISA", bg="grey", width = '300', height = '2', font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", width = '30', height = '2', command = login).pack()
    Label(text="").pack()
    Button(text="Register", width = '30', height = '2', command = register).pack()

    screen.mainloop()


main_screen()

