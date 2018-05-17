from Tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class GraphGUI:
    def __init__(self, loginGUI):
        self.window = Tk()
        self.prev = loginGUI
        self.window.title("Coffee Cup Detector")
        self.window.geometry("500x500")

    def yearlyGraph(self):
        self.window.withdraw()
        yearlyGraphGUI = YearlyGraphGUI(self.window)
        yearlyGraphGUI.createYearlyGraphGUI()
        
    def monthlyGraph(self):
        self.window.withdraw()
        monthlyGraphGUI = MonthlyGraphGUI(self.window)
        monthlyGraphGUI.createMonthlyGraphGUI()
    
    def dailyGraph(self):
        self.window.withdraw()
        dailyGraphGUI = DailyGraphGUI(self.window)
        dailyGraphGUI.createDailyGraphGUI()
    
    def backButtonAction(self):
        self.window.withdraw()
        self.prev.deiconify()
        

    def createGraphGUI(self):
        
        backBtn = Button(self.window, text="Back", width=20, command=self.backButtonAction)
        backBtn.grid(row=0, column=0)
    
        yearBtn = Button(self.window, text="Yearly Graph", width=20, command=self.yearlyGraph)
        yearBtn.grid(row=1, column=0)

        monthlyBtn = Button(self.window, text="Monthly Graph", width=20, command=self.monthlyGraph)
        monthlyBtn.grid(row=2, column=0)
        
        dailyBtn = Button(self.window, text="Daily Graph", width=20, command=self.dailyGraph)
        dailyBtn.grid(row=3, column=0)
        self.window.mainloop()

class YearlyGraphGUI:
    
    def backButtonAction(self):
        self.window.withdraw()
        self.prev.deiconify()
    
    def __init__(self, menuGUI):
        self.prev = menuGUI
        self.window = Tk()
        self.window.title("Yearly Graph")
        self.window.geometry("500x500")
        backBtn = Button(self.window, text="Back", width=20, command=self.backButtonAction)
        backBtn.pack()
        
    def createYearlyGraphGUI(self):
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[15,6,11,3,8,9,3,15])
        
        canvas = FigureCanvasTkAgg(f, self.window)
        canvas.show()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
        
        toolbar = NavigationToolbar2TkAgg(canvas, self.window)
        toolbar.update()
        canvas._tkcanvas.pack(side=TOP, fill = BOTH, expand=True)
        
        
class MonthlyGraphGUI:
    
    def backButtonAction(self):
        self.window.withdraw()
        self.prev.deiconify()
    
    def __init__(self, menuGUI):
        self.prev = menuGUI
        self.window = Tk()
        self.window.title("Monthly Graph")
        self.window.geometry("500x500")
        backBtn = Button(self.window, text="Back", width=20, command=self.backButtonAction)
        backBtn.pack()
        
    def createMonthlyGraphGUI(self):
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[15,6,11,3,8,9,3,15])
        
        canvas = FigureCanvasTkAgg(f, self.window)
        canvas.show()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
        
        toolbar = NavigationToolbar2TkAgg(canvas, self.window)
        toolbar.update()
        canvas._tkcanvas.pack(side=TOP, fill = BOTH, expand=True)
        
class DailyGraphGUI:
    
    def backButtonAction(self):
        self.window.withdraw()
        self.prev.deiconify()
    
    def __init__(self, menuGUI):
        self.prev = menuGUI
        self.window = Tk()
        self.window.title("Daily Graph")
        self.window.geometry("500x500")
        
        backBtn = Button(self.window, text="Back", width=20, command=self.backButtonAction)
        backBtn.pack()
        
    def createDailyGraphGUI(self): 
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[15,6,11,3,8,9,3,15])
        
        canvas = FigureCanvasTkAgg(f, self.window)
        canvas.show()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
        
        toolbar = NavigationToolbar2TkAgg(canvas, self.window)
        toolbar.update()
        canvas._tkcanvas.pack(side=TOP, fill = BOTH, expand=True)    