from tkinter import *
from customtkinter import *
import tkinter
import customtkinter
from tkinter import ttk
from PIL import ImageTk, Image
import sqlite3
from main import mainScreen


textcolor = "whitesmoke"
cnxt = sqlite3.connect("data/userdata.db")
c = cnxt.cursor()
# c.execute("drop table recipedata")
c.execute("CREATE TABLE IF NOT EXISTS userdata (USERNAME TEXT PRIMARY KEY NOT NULL UNIQUE, FIRSTNAME TEXT NOT NULL, LASTNAME TEXT NOT NULL, EMAIL TEXT NOT NULL, PASSWORD TEXT NOT NULL)")


def loginPage():
    global bgImage
    window = CTk()

# app height and width
    appWidth = 360
    appHeight = 470
# getting the screen height and width
    screenHeight = window.winfo_screenheight()
    screenWidth = window.winfo_screenwidth()
# x and y co-ordinates
    centerX = (screenWidth/2)-(appWidth/2)
    centerY = (screenHeight/2)-(appHeight/2)
# centering the app on screen

    window.geometry(f"{appWidth}x{appHeight}+{int(centerX)}+{int(centerY)}")
    window.resizable(False, False)
    window.title("login")

# functions
    # navigate to registerpage
    def navigate():
        window.destroy()
        registerPage()

    def getUserData():
        global credentials
        username = usernameEntry.get().lower()
        password = passwordEntry.get()

        c.execute("select * from userdata where USERNAME='" +
                  username+"' and PASSWORD='"+password+"'")
        userdata = c.fetchall()

        if userdata != []:
            for user in userdata:
                if username and password in user:
                    def fetchUser():
                        global credentials
                        window.destroy()
                        credentials = user[0]
                        mainScreen()
                    fetchUser()
        else:
            errorLabel.configure(text="username or password incorrect",
                                 bg_color="lightpink", text_color="firebrick")
            errorLabel.after(5000, lambda: errorLabel.configure(
                text="", bg_color="#2B2B2B"))


# functions

    # login frame

    frame1 = customtkinter.CTkFrame(
        window, height=appHeight, width=appWidth, bg_color="black")
    frame1.pack(fill="both")
    frame1.pack_propagate(False)
    # login title
    loginLabel = customtkinter.CTkLabel(master=frame1, text="Sign In !", font=(
        "helvatica", 20, "bold"), text_color=textcolor)
    loginLabel.place(x=26, y=20)
    # login image
    bgImage = customtkinter.CTkImage(
        light_image=Image.open("Assets/4.png"), size=(175, 141))
    imgWidget = customtkinter.CTkLabel(master=frame1, image=bgImage, text="")
    imgWidget.pack(pady=55, fill="both")
    # error label
    errorLabel = customtkinter.CTkLabel(
        master=frame1, text="", width=300, height=25)
    errorLabel.place(y=200, x=25)
    # username entry

    usernameEntry = customtkinter.CTkEntry(
        master=frame1, placeholder_text="username", width=300, height=35,)
    usernameEntry.place(y=250, x=25)

    # password entry
    passwordEntry = customtkinter.CTkEntry(
        master=frame1, placeholder_text="password", width=300, height=35)
    passwordEntry.place(y=300, x=25)

    # login button
    loginbtn = customtkinter.CTkButton(
        master=frame1, text="Login", width=300, height=35, command=getUserData)
    loginbtn.place(y=350, x=25)
    # navigate to registration form
    registerLabel = customtkinter.CTkLabel(
        master=frame1, text="Dont have an account?", font=("helvatica", 16))
    registerLabel.place(y=405, x=25)
    registerBtn = customtkinter.CTkButton(
        master=frame1, text="Register now", width=120, command=navigate)
    registerBtn.place(x=204, y=405)

    window.mainloop()


def registerPage():
    global registerImg
    window = CTk()

    registerImg = customtkinter.CTkImage(
        light_image=Image.open("Assets/5.png"), size=(250, 250))

    # window width and height
    appWidth = 850
    appHeight = 500
    # screen height and width
    screenHeight = window.winfo_screenheight()
    screenWidth = window.winfo_screenwidth()
    # x and y co-ordinates of page
    centerX = (screenWidth/2)-(appWidth/2)
    centerY = (screenHeight/2)-(appHeight/2)
    # centering the window on the screen
    window.geometry(f"{appWidth}x{appHeight}+{int(centerX)}+{int(centerY)}")
    window.resizable(False, False)
    window.title("register")
    # fucntion

    def navigate():
        window.destroy()
        loginPage()

    def getUserData():
        # store user credentialls into variables
        firstname = registerFirstName.get().lower()
        lastname = registerLastName.get().lower()
        username = registerusername.get().lower()
        email = registeremail.get().lower()
        password = registerpassword.get()
        confirmpassword = registerconfirmpassword.get()

        # call database
        c.execute("select * from userdata where USERNAME='"+username+"'")
        dataResult = c.fetchall()
        # collect all userdata variable into a list
        userData = [
            (firstname),
            (lastname),
            (username),
            (email),
            (password),
        ]

        # verify and validate user and store user into database
        if dataResult == []:
            if firstname == "" or lastname == "" or username == "empty" or password == "" or email == "" or confirmpassword == "":
                errorLabel.configure(
                    text="please enter all the form fields", bg_color="lightpink", text_color="firebrick")
                errorLabel.after(5000, lambda: errorLabel.configure(
                    text="", bg_color="#2B2B2B"))
            elif len(firstname) <= 3 or len(lastname) <= 3 or len(username) <= 3:
                errorLabel.configure(text="username, firstname and lastname must be more than 3 letters",
                                     bg_color="lightpink", text_color="firebrick")
                errorLabel.after(5000, lambda: errorLabel.configure(
                    text="", bg_color="#2B2B2B"))
            elif "." and "@" not in email:
                errorLabel.configure(
                    text="invalid email address", bg_color="lightpink", text_color="firebrick")
                errorLabel.after(5000, lambda: errorLabel.configure(
                    text="", bg_color="#2B2B2B"))
            elif len(password) <= 5:
                errorLabel.configure(text="password must me longer than 5 character",
                                     bg_color="lightpink", text_color="firebrick")
                errorLabel.after(5000, lambda: errorLabel.configure(
                    text="", bg_color="#2B2B2B"))
            elif password != confirmpassword:
                errorLabel.configure(
                    text="password does not match", bg_color="lightpink", text_color="firebrick")
                errorLabel.after(5000, lambda: errorLabel.configure(
                    text="", bg_color="#2B2B2B"))
            else:
                c.execute(
                    "insert into userdata (FIRSTNAME, LASTNAME, USERNAME, EMAIL, PASSWORD) values(?,?,?,?,?)", (userData))
                cnxt.commit()
                errorLabel.configure(
                    text="registration successful", bg_color="lightgreen", text_color="darkgreen")
                errorLabel.after(5000, lambda: errorLabel.configure(
                    text="", bg_color="#2B2B2B"))
        else:
            errorLabel.configure(text="username has already been taken, please select a new username",
                                 bg_color="lightpink", text_color="firebrick")
            errorLabel.after(5000, lambda: errorLabel.configure(
                text="", bg_color="#2B2B2B"))

        registerFirstName.delete(0, END)
        registerLastName.delete(0, END)
        registerusername.delete(0, END)
        registeremail.delete(0, END)
        registerpassword.delete(0, END)
        registerconfirmpassword.delete(0, END)

    # fucntion

    # image frame
    imageFrame = customtkinter.CTkFrame(
        master=window, height=appHeight, width=.35*appWidth,)
    imageFrame.place(x=0, y=0)
    imageFrame.propagate(False)
    # image label
    imgWidget = customtkinter.CTkLabel(
        master=imageFrame, image=registerImg, height=appHeight, width=.35*appWidth, text="")
    imgWidget.pack(padx=20)

    # form Frame
    formFrame = customtkinter.CTkFrame(
        master=window, height=appHeight, width=.65*appWidth)
    formFrame.place(x=296, y=0)
    formFrame.pack_propagate(False)
    formFrame.propagate(False)
    # registration title
    registerTitle = customtkinter.CTkLabel(master=formFrame, text="Sign up...!", font=(
        "helvatica", 25, "bold"), text_color=textcolor)
    registerTitle.place(x=50, y=25)
    # errorLabel
    errorLabel = customtkinter.CTkLabel(master=formFrame, text="", width=420)
    errorLabel.place(y=90, x=57)
    # input fields
    # firstname
    registerFirstName = customtkinter.CTkEntry(
        master=formFrame, width=205, placeholder_text="first name", height=30)
    registerFirstName.place(x=57, y=140)
    # lastname
    registerLastName = customtkinter.CTkEntry(
        master=formFrame, width=205, placeholder_text="last name", height=30)
    registerLastName.place(x=270, y=140)
    # username
    registerusername = customtkinter.CTkEntry(
        master=formFrame, width=417, placeholder_text="username", height=30)
    registerusername.place(x=57, y=190)
    # email
    registeremail = customtkinter.CTkEntry(
        master=formFrame, width=417, placeholder_text="email", height=30)
    registeremail.place(x=57, y=240)
    # password
    registerpassword = customtkinter.CTkEntry(
        master=formFrame, width=417, placeholder_text="password", height=30)
    registerpassword.place(x=57, y=290)
    # confirm password
    registerconfirmpassword = customtkinter.CTkEntry(
        master=formFrame, width=417, placeholder_text="confirm-password", height=30)
    registerconfirmpassword.place(x=57, y=340)
    # register button
    registerBtn = customtkinter.CTkButton(
        master=formFrame, text="Sign up", width=417, height=30, command=getUserData)
    registerBtn.place(x=57, y=390)
    # navigate to login form
    loginLabel = customtkinter.CTkLabel(
        master=formFrame, text="Dont  have  an  account  ?", font=("helvatica", 16, "bold"))
    loginLabel.place(x=57, y=440)
    registerBtn = customtkinter.CTkButton(
        master=formFrame, text="login", width=200, command=navigate)
    registerBtn.place(x=270, y=440)

    window.mainloop()


# loginPage()
