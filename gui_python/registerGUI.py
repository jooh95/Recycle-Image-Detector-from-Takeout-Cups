from Tkinter import *
from connectModule import *

class RegisterGUI:
    
    def __init__(self, loginGUI):
        self.window =  Tk()
        self.prev = loginGUI
        self.idInput = Entry(self.window)
        self.pwdInput = Entry(self.window, show = '*')
        self.nameInput = Entry(self.window)
        self.fRegionInput = Entry(self.window)
        self.fNameInput = Entry(self.window)
        
    def ok(self):
        self.window.withdraw()
        insertDB(self.idInput.get(), self.pwdInput.get(), self.nameInput.get(), self.fRegionInput.get(), self.fNameInput.get())
        self.prev.deiconify()
        
    def cancel(self):
        self.window.withdraw()
        self.prev.deiconify()
        
    def createRegisterGUI(self):
    
        self.window.title("Register")
        self.window.geometry("500x500")

        idLabel = Label(self.window, text="id")
        idLabel.grid(row=1, column=0)

        self.idInput.grid(row=1, column=1, sticky='NS')

        pwdLabel = Label(self.window, text="pwd")
        pwdLabel.grid(row=2, column=0)

        self.pwdInput.grid(row=2, column=1)
        
        nameLabel = Label(self.window, text="name")
        nameLabel.grid(row=3, column=0)

        self.nameInput.grid(row=3, column=1, sticky='NS')
        
        fRegionLabel = Label(self.window, text="factory region")
        fRegionLabel.grid(row=4, column=0)

        self.fRegionInput.grid(row=4, column=1, sticky='NS')
        
        fNameLabel = Label(self.window, text="factory name")
        fNameLabel.grid(row=5, column=0)

        self.fNameInput.grid(row=5, column=1, sticky='NS')

        okBtn = Button(self.window, text="ok", width=20, command=self.ok)
        okBtn.grid(row= 6, column=0)
        
        cancelBtn = Button(self.window, text="cancel", width=20, command=self.cancel)
        cancelBtn.grid(row= 6, column=1)
        
        self.window.mainloop()