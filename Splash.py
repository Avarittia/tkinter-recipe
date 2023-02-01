from tkinter import *
from customtkinter import *
import customtkinter
from PIL import ImageTk , Image
from form import loginPage



splashScreen=CTk()

splashScreen.title("splashscreen")
splashScreen.overrideredirect(True)# True value makes the titlebar dissapear

#getting the value of screen
screenWidth= splashScreen.winfo_screenwidth()
screenHeight= splashScreen.winfo_screenheight()

#height and width of the app

splashScreenWidth=350
splashScreenHeight=400

#x and y co-ordinates of app

splashScreenX=(screenWidth/2)-(splashScreenWidth/2)
splashscreenY=(screenHeight/2)-(splashScreenHeight/2)

def killWindow():
    splashScreen.destroy()
    loginPage()

#placing the app at the center

splashScreen.geometry(f"{splashScreenWidth}x{splashScreenHeight}+{int(splashScreenX)}+{int(splashscreenY)}")

#adding image
bgImage=customtkinter.CTkImage(light_image=Image.open("Assets/1.png"),size=(300, 300))

#adding background to the label
bgLabel=customtkinter.CTkLabel(splashScreen, text="", image=bgImage)
bgLabel.pack(fill=BOTH)
bgLabel.pack_propagate(False)


splashScreen.after(3000, killWindow)



splashScreen.mainloop()


