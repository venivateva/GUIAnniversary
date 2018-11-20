from tkinter import*
import tkinter.messagebox
import tkinter.colorchooser


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.pack()


    def love_love(self):
        love=input("What is your name?")
        print(love+" +Veni = <3!!")


    def createWidgets(self):
        self.hi_there = Button(self)
        self.hi_there["text"] = "CLICK ME",
        self.hi_there["fg"]="green"
        self.hi_there["command"] = self.love_love

        self.hi_there.pack({"side": "left"})

    #def __init__(self, master=None):
        #Frame.__init__(self, master)
        #self.pack()
        #self.createWidgets()

#root=Tk()
myapp = Application()
myapp.master.title("Happy Anniversary!")
myapp.master.geometry('500x300+200+200')
myapp.mainloop()