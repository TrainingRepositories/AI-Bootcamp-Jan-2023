__author__ = 'rich'

from tkinter import *
import sqlite3

class Application(Frame):

   def __init__(self, master):
       super(Application, self).__init__(master)
       self.grid()

       self.conn = sqlite3.connect("pizza.db")
       self.cursor = self.conn.cursor()
       self.prices = {'medium':0,
                      'large':0,
                      'x-large':0,
                      'med-topping':0,
                      'large-topping':0,
                      'xl-topping':0}
       for row in self.cursor.execute("SELECT * FROM prices"):
          self.prices[row[0]] = row[1]
       self.conn.close()
       self.create_widgets()

   def create_widgets(self):
       self.label0 = Label(self, text="Pizza Calculator Prices")
       self.label0.grid(row=0, column=0, columnspan=2, sticky=W)

       self.heading1 = Label(self, text="Price")
       self.heading1.grid(row=1, column=1, sticky=W)
       self.heading2 = Label(self, text="Toppings")
       self.heading2.grid(row=1, column=2, sticky=W)

       self.label1 = Label(self, text="Medium")
       self.label1.grid(row=2, column=0, sticky=W)
       self.med = Entry(self, width=5)
       self.med.grid(row=2, column=1, sticky=W)
       self.med.insert(END, self.prices["medium"])
       self.medtop = Entry(self, width=5)
       self.medtop.grid(row=2, column=2, sticky=W)
       self.medtop.insert(END, self.prices["med-topping"])

       self.label2 = Label(self, text="Large")
       self.label2.grid(row=3, column=0, sticky=W)
       self.large = Entry(self, width=5)
       self.large.grid(row=3, column=1, sticky=W)
       self.large.insert(END, self.prices["large"])
       self.largetop = Entry(self, width=5)
       self.largetop.grid(row=3, column=2, sticky=W)
       self.largetop.insert(END, self.prices["large-topping"])

       self.label3 = Label(self, text="X-Large")
       self.label3.grid(row=4, column=0, sticky=W)
       self.xl = Entry(self, width=5)
       self.xl.grid(row=4, column=1, sticky=W)
       self.xl.insert(END, self.prices["x-large"])
       self.xltop = Entry(self, width=5)
       self.xltop.grid(row=4, column=2, sticky=W)
       self.xltop.insert(END, self.prices["xl-topping"])

window = Tk()
window.title("Python Pizza Prices")
window.geometry("330x175")
app = Application(window)
app.mainloop()