#https://www.youtube.com/watch?v=5sEm7RcRF_g
#https://www.youtube.com/watch?v=clP6W7W79MM
#https://www.youtube.com/watch?v=t9Ed5QyO7qY
#https://www.geeksforgeeks.org/python-get-google-map-image-specified-location-using-google-static-maps-api/
#https://python-visualization.github.io/folium/         -- Documentation
#https://www.youtube.com/watch?v=fSglTrjhNYs            -- Google maps plotting points
#https://www.youtube.com/watch?v=QpBmO35pmVE&list=PL2UmzTIzxgL5LiQHwUFtf9mun2I99jdc-&index=1    -- Folium full tutorial



from tkinter import *
import pyrebase

#Web APP Credentials for Firebase connection
firebaseConfig ={'apiKey': "AIzaSyDDOUUPzA2OuTT9deZcHCtBe88C3JmHUOI",
    'authDomain': "aisa-4b073.firebaseapp.com",
    'databaseURL': "https://aisa-4b073-default-rtdb.firebaseio.com",
    'projectId': "aisa-4b073",
    'storageBucket': "aisa-4b073.appspot.com",
    'messagingSenderId': "714681750998",
    'appId': "1:714681750998:web:9b195c244d9fd2b64a4077",
    'measurementId': "G-E7WH5S8B7P"}

firebase = pyrebase.initialize_app(firebaseConfig)




#Registration authentication function
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
        
        data = {'Name': name1, 'Vehicle_no': vehicle_no1, 'RC_Book_no': rc_book_no1, 'DL_no': dl_no1, 'Username': username_info, 'Balance': '0'}
        db.child('Users').child(vehicle_no1).set(data)
        
        print("Registration Sucessfull")
        
        screen1.destroy()
    
    except:
        msg = Message(screen1, text = "Registration Unsucessfull!")  
        msg.pack()






#Registration main page
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title ("A.I.S.A")
    screen1.geometry ("500x500")

    global username,password,name,vehicle_no,rc_book_no,dl_no

    username = StringVar()
    password = StringVar()
    name =  StringVar()
    vehicle_no = StringVar()
    rc_book_no = StringVar()
    dl_no = StringVar()

    Label(screen1,text="Register", bg="#303030", fg = "white", width = '300', height = '2', font=("Roboto", 13)).pack()
    Label(text="").pack()
    Label(screen1,text="Name").pack()
    Entry(screen1,textvariable = name).pack()
    Label(screen1,text="Vehicle Number").pack()
    Entry(screen1,textvariable = vehicle_no).pack()
    Label(screen1,text="RC Book Number").pack()
    Entry(screen1,textvariable = rc_book_no).pack()
    Label(screen1,text="Driving License Number").pack()
    Entry(screen1,textvariable = dl_no).pack()
    Label(screen1,text="Email").pack()
    Entry(screen1,textvariable = username).pack()
    Label(screen1,text="Password").pack()
    Entry(screen1,textvariable = password,show='*').pack()
    Label(text="").pack()
    Button(screen1, text = "Register", width =10, height = 1, command = register_user).pack()


def recharge():
    print("Recharge sucessfull")


#Screen after sucessfull login
def logged_in():
    db= firebase.database()

    login_vehicle_no1 = login_vehicle_no.get()

    screen3 = Toplevel(screen)
    screen3.title("A.I.S.A")
    screen3.geometry("1000x800")
    Label(screen3,text="").pack()

    #Pulling data from database according to vehicle number
    users = db.child("Users").child(login_vehicle_no1).get()
    #Sperating values
    dict1 = users.val()
    dl_no_logged_in = dict1['DL_no']
    name_logged_in = dict1['Name']
    rc_book_no_logged_in = dict1['RC_Book_no']
    balance_logged_in = dict1['Balance']

    Label(screen3,text="Vehicle Number  :  "+str(login_vehicle_no1), font=("Roboto", 13)).place(x=20,y=20)
    Label(screen3,text="Balance : "+str(balance_logged_in), font=("Roboto", 13)).place(x=825,y=20)
    Button(screen3, text = "Recharge", width =11, height = 1, command = recharge, font=("Roboto", 10), bg = '#202020', fg='#ffffff').place(x=825,y=60)



#Login authentication function
def login_user():
    auth = firebase.auth()

    username = login_username.get()
    password = login_password.get()

    try:
        login = auth.sign_in_with_email_and_password(username, password)
        msg = Message(screen2, text = "Login sucessfull!")  
        msg.pack()
        print("Login Sucessfull")
        logged_in()
        screen2.destroy()
    except:
        msg = Message(screen2, text = "Wrong Username/Password")  
        msg.pack()





#Login main screen
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title ("A.I.S.A")
    screen2.geometry ("500x500")
    
    global login_username, login_password, login_vehicle_no

    login_username = StringVar()
    login_password = StringVar()
    login_vehicle_no = StringVar()

    Label(screen2,text="Login", bg="#303030", fg = "white", width = '300', height = '2', font=("Roboto", 13)).pack()
    Label(screen2,text="").pack()
    Label(screen2,text="").pack()
    Label(screen2,text="Email", font=("Roboto", 10)).pack()
    Entry(screen2,textvariable = login_username, width=30).pack()
    Label(screen2,text="").pack()
    Label(screen2,text="Vehicle Number", font=("Roboto", 10)).pack()
    Entry(screen2,textvariable = login_vehicle_no, width=30).pack()
    Label(screen2,text="").pack()
    Label(screen2,text="Password", font=("Roboto", 10)).pack()
    Entry(screen2,textvariable = login_password,show='*',width=30).pack()
    Label(screen2,text="").pack()
    Button(screen2, text = "Login", width =30, height = 2, command = login_user, font=("Roboto", 10)).pack()




def main_screen():
    global screen
    screen = Tk()
    screen.geometry("500x500")
    screen.title("A.I.S.A")
    Label(text="An Intelligent System for Automobiles", bg="#303030", fg = "white", width = '300', height = '3', font=("Roboto", 18)).pack()
    Label(text="").pack()
    Button(text="Login", width = '30', height = '2', command = login, font=("Roboto", 14, 'bold'), bg = '#BEBEBE', fg = '#000033').pack()
    Label(text="").pack()
    Button(text="Register", width = '30', height = '2', command = register, font=("Roboto", 14, 'bold'), bg = '#BEBEBE', fg = '#000033').pack()
    #logged_in()
    screen.mainloop()


main_screen()

