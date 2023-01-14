__author__ = 'rich'

from tkinter import *
import sqlite3

class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.toppings = []
        self.prices = {"medium":0,
                       "large":0,
                       "x-large":0,
                       "med-topping":0,
                       "large-topping":0,
                       "xl-topping":0}
        self.conn = sqlite3.connect("pizza.db")
        self.cursor = self.conn.cursor()

        for row in self.cursor.execute("SELECT * FROM toppings ORDER BY topping"):
            self.toppings.append(row[0])
        for row in self.cursor.execute("SELECT * FROM prices"):
            self.prices[row[0]] = row[1]
        self.conn.close()

        self.checkbox = list(self.toppings)
        self.checkboxVar = list(self.toppings)
        self.create_widgets()

    def create_widgets(self):
        self.label1 = Label(self, text="Select Size:")
        self.label1.grid(row=0, column=0, sticky=W)

        self.size = StringVar()

        self.radio1 = Radiobutton(self,
                                  text="Medium",
                                  variable = self.size,
                                  value="Medium")
        self.radio1.grid(row=1, column=0, sticky=W)
        self.radio1.select()

        self.radio2 = Radiobutton(self,
                                  text="Large",
                                  variable = self.size,
                                  value="Large")
        self.radio2.grid(row=1, column=1, sticky=W)

        self.radio3 = Radiobutton(self,
                                  text="Extra Large",
                                  variable = self.size,
                                  value="X-Large")
        self.radio3.grid(row=1, column=2, sticky=W)

        self.label2 = Label(self, text='Select Toppings:')
        self.label2.grid(row=2, column=0, sticky=W)

        line = 2
        for i in range(len(self.toppings)):
            line = line + 1
            self.checkboxVar[i] = BooleanVar()
            self.checkbox[i] = Checkbutton(self,
                                           text=self.toppings[i],
                                           variable=self.checkboxVar[i])
            self.checkbox[i].grid(row=line, column=0, sticky=W)

        line = line + 1
        self.button1 = Button(self, text="Reset", command=self.reset)
        self.button1.grid(row=line, column=0)
        self.button2 = Button(self, text="Calculate Price", command=self.calculate)
        self.button2.grid(row=line, column=1)

        line = line + 1
        self.label3 = Label(self, text="")
        self.label3.grid(row=line, column=0)

        line = line + 1
        self.label4 = Label(self, text="Total:")
        self.label4.grid(row=line, column=0, sticky=E)
        self.result = Entry(self, width=10)
        self.result.grid(row=line, column=1, sticky=W)

    def reset(self):
        """Reset the Radiobuttons, Checkbuttons, and Entry box"""
        self.radio1.select()
        for i in range(len(self.toppings)):
           self.checkbox[i].deselect()
        self.result.delete(0,END)

    def calculate(self):
        """Event handler for the calculator"""
        self.totalToppings = 0
        for i in range(len(self.toppings)):
           if (self.checkboxVar[i].get()):
              self.totalToppings = self.totalToppings + 1

        if (self.size.get() == "Medium"):
              self.price = self.prices["medium"] + (self.totalToppings * self.prices["med-topping"])
        elif (self.size.get() == "Large"):
              self.price = self.prices["large"] + (self.totalToppings * self.prices["large-topping"])
        elif (self.size.get() == "X-Large"):
              self.price = self.prices["x-large"] + (self.totalToppings * self.prices["xl-topping"])

        strPrice = "{0:.2f}".format(self.price)
        self.result.delete(0, END)
        self.result.insert(END, strPrice)

window = Tk()
window.title("Python Pizza Calculator")
window.geometry('300x345')
app = Application(window)
app.mainloop()