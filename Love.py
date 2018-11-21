from tkinter import*
import tkinter.messagebox
import tkinter.colorchooser



class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.pack()

    


    def createWidgets(self):
        self.hi_there = Button(self)
        self.hi_there["text"] = "CLICK ME"
        self.hi_there["fg"] = "green"
        self.hi_there["cursor"]="heart"
        self.hi_there["command"] = self.love_output
        self.hi_there["relief"]="ridge"
        self.hi_there.grid(column=1,row=4)

        self.QUIT = Button(self)
        self.QUIT["text"]= "QUIT"
        self.QUIT["fg"]= "red"
        self.QUIT["cursor"]= "spider"
        self.QUIT["command"]= self.quit
        self.QUIT.grid(column=1, row=5)

        self.pic= Button(self)
        self.pic["text"]= "SLOTHS!!"
        self.pic["fg"]="brown"
        self.pic["command"]=self.sloth
        self.pic.grid(column=1, row=6)


        self.labeling= Label(self)
        self.labeling["text"]="What is your name?"
        self.labeling["fg"] = "orange"
        self.labeling["height"]="4"
        self.labeling.grid(row=0)


        self.labeling = Label(self)
        self.labeling["text"] = "Who is your favorite?"
        self.labeling["fg"] = "orange"
        self.labeling["height"] = "4"
        self.labeling.grid(row=1)

        self.entering1=Entry(self)
        self.entering1.grid(row=0,column=1)

        self.entering2=Entry(self)
        self.entering2.grid(row=1, column=1)


        self.canvas = Canvas(width=300,height=300,bg="green")
        pic1=PhotoImage(file="sloth.gif")
        self.canvas.create_image(50,10,image=pic1)

    def sloth(self):
        top = Toplevel()
        photos = PhotoImage(file="sloth.gif")
        sloth = Label(top, image=photos)
        sloth.grid()
        sloth.mainloop()

    def love_output(self):

        fieldValue1 = self.entering1.get()
        fieldValue2=self.entering2.get()
        tkinter.messagebox.showinfo("Happy Anniversary",fieldValue1+"+"+fieldValue2+" = <3")
        return


myapp = Application()
myapp.master.title("Happy Anniversary!")
myapp.master.geometry('500x300+200+200')
myapp.mainloop()