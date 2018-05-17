from Tkinter import *
from graphGUI import *
from registerGUI import *
from connectModule import *

class LoginGUI:
    
    def __init__(self):
        self.window =  Tk()
        self.idInput = Entry(self.window)
        self.pwdInput = Entry(self.window, show = '*')
    
    def login(self):
        print(self.pwdInput.get())
        #if(getLoginResult(self.idInput.get(), self.pwdInput.get())):
        if(True):
            self.window.withdraw()
            graphGUI = GraphGUI(self.window)
            graphGUI.createGraphGUI()
        
    def register(self):
        self.window.withdraw()
        registerGUI = RegisterGUI(self.window)
        registerGUI.createRegisterGUI()
    
    def createLoginGUI(self):
    
        self.window.title("Login")
        self.window.geometry("500x500")
        
        #img = PhotoImage(file="/Users/caucse/Desktop/New/icon_image.gif")
        #icon = Label(self.window, image=img)
        #icon.grid(row=0,column=1)

        idLabel = Label(self.window, text="id")
        idLabel.grid(row=1, column=0)

        self.idInput.grid(row=1, column=1, sticky='NS')

        pwdLabel = Label(self.window, text="pwd")
        pwdLabel.grid(row=2, column=0)

        
        self.pwdInput.grid(row=2, column=1)

        loginBtn = Button(self.window, text="login", width=20, command=self.login)
        #loginBtn.bind('<Button>', self.login)
        #loginBtn.bind('<Return>', login)
        loginBtn.grid(row= 3, column=0)
        
        registerBtn = Button(self.window, text="register", width=20, command=self.register, fg= "white", bg="green")
        registerBtn.grid(row= 3, column=1)
        
        self.window.mainloop()
        
loginGUI = LoginGUI()
loginGUI.createLoginGUI()
