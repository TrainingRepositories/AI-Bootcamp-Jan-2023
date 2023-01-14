__author__ = 'rich'

import sqlite3

conn = sqlite3.connect("pizza.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE toppings (topping varchar(15) primary key)")
cursor.execute("CREATE TABLE prices (product varchar(15) primary key, price decimal)")

sql = ("INSERT INTO toppings (topping) VALUES(?)")
toppings = [('Sausage',),
            ('Pepperoni',),
            ('Chicken',),
            ('Mushroom',),
            ('Black Olive',),
            ('Green Pepper',),
            ('Red Pepper',),
            ('Onion',)]
cursor.executemany(sql, toppings)

sql = ("INSERT INTO prices (product, price) VALUES (?, ?)")
prices = [('medium', '9.99'),
          ('large', '12.99'),
          ('x-large', '14.99'),
          ('med-topping', '1.00'),
          ('large-topping', '1.50'),
          ('xl-topping', '1.80')]
cursor.executemany(sql, prices)

conn.commit()
conn.close()