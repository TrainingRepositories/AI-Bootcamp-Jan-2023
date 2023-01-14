__author__ = 'rich'

from tkinter import *

class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        menubar = Menu(self)
        filemenu = Menu(menubar)
        filemenu.add_command(label="Submit", command=self.process)
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_command(label="Quit", command=window.quit)
        self.label1 = Label(self, text="Instruct the delivery person to:")
        self.label1.grid(row=0, column=0)
        self.entry1 = Entry(self, width=50)
        self.entry1.grid(row=0, column=1)
        self.entry1.focus()
        self.button1 = Button(self, text="Submit", command=self.process)
        self.button1.grid(row=0, column=2)
        self.label2 = Label(self, width=60)
        self.label2.grid(row=2, columnspan=3, sticky=S)
        window.config(menu=menubar)

    def process(self):
        instructions = self.entry1.get()
        output = "The delivery person will be instructed to \"" + instructions + "\""
        self.label2['text'] = output

window = Tk()
window.title("Pizza Delivery Instructions")
window.geometry("550x70")
app = Application(window)
app.mainloop()