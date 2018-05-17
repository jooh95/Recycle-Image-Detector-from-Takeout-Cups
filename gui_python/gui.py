from loginGUI import *
import time

def main():
    root = Tk()
    root.title('Coffe Cup Recycler')
    root.geometry('500x400+10+10')
    mainFrame = MainFrame(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
    time.sleep(100)
    createLoginGUI()
    
