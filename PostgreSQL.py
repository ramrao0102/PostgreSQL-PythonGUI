
# This is a work in  progress and it will be 
# geeralized in a few days time

# -*- coding: utf-8 -*-
"""
Created on Mon May 23 06:28:17 2022

@author: ramra
"""

from tkinter import *
import psycopg2

root = Tk()

root.title('Ram Rao - Connectivity to PostgreSQL Database')

root.geometry("600x600")

# Database connectivity stuff

conn = psycopg2.connect(database="kineteco",
                        host="localhost",
                        user="postgres",
                        password="Sachin10,dulkar",
                        port="5432")

cursor = conn.cursor()

# Function for Inserting Records into Database

def submit():
    
    conn = psycopg2.connect(database="kineteco",
                            host="localhost",
                            user="postgres",
                            password="Sachin10,dulkar",
                            port="5432")

    cursor = conn.cursor()
        
    # Insert into Table
    # this can be modified as needed so any record in database can be updated
        
    sql = "INSERT INTO manufacturing.products (product_id, product_name, power, manufacturing_cost, category_id) VALUES (%s, %s, %s, %s, %s)"
    val = (product_id.get(), product_name.get(), power.get(), manufacturing_cost.get(), category_id.get())
    
    cursor.execute(sql, val)
      
    #Commit changes
    
    conn.commit()
    print("Record Inserted")
        
    # Close Connection
    
    conn.close()
        
    #clear the Text Boxes
    product_id.delete(0, END)
    product_name.delete(0, END)
    power.delete(0, END)
    manufacturing_cost.delete(0, END)
    category_id.delete(0, END)
    
# Function for Querying the database    
    
def query():

    conn = psycopg2.connect(database="kineteco",
                        host="localhost",
                        user="postgres",
                        password="Sachin10,dulkar",
                        port="5432")

    cursor = conn.cursor()    

    cursor.execute("SELECT * FROM manufacturing.products")    
    
    rows = cursor.fetchmany(5)
    
    # loop through results
    
    print_records = ''
    
    for record in rows:
        print_records += str(record) + "\n"
        
    
    query_label = Label(my_frame, text = print_records)
    
    query_label.grid(row =5, column = 0, columnspan = 2)
    
    conn.commit()
    
    conn.close()

# Function for Updating the database

def update():
   
    conn = psycopg2.connect(database="kineteco",
                       host="localhost",
                       user="postgres",
                       password="Sachin10,dulkar",
                       port="5432")

    cursor = conn.cursor() 
   
    
    cursor.execute ("UPDATE manufacturing.products SET category_id = 2 WHERE category_id = 1")
    
    conn.commit()
    
    conn.close()
   
    
# Tkinter Frame Building Stuff

# Building the Frame

my_frame = LabelFrame(root, text = "Postgres Connection")
my_frame.pack(pady=20)

product_id = Label(my_frame, text = "Product_ID:")
product_id.grid(row=0, column=0, pady=10, padx=10)

product_id = Entry(my_frame, font = ("Helvetica, 12"))
product_id.grid(row=0, column =1, pady=10, padx=10)

product_name = Label(my_frame, text = "Product_Name:")
product_name.grid(row=1, column=0, pady=10, padx=10)

product_name = Entry(my_frame, font = ("Helvetica, 12"))
product_name.grid(row=1, column =1, pady=10, padx=10)

power = Label(my_frame, text = "Power:")
power.grid(row=0, column=2, pady=10, padx=10)

power = Entry(my_frame, font = ("Helvetica, 12"))
power.grid(row=0, column =3, pady=10, padx=10)

manufacturing_cost = Label(my_frame, text = "Manufacturing Cost:")
manufacturing_cost.grid(row=1, column=2, pady=10, padx=10)

manufacturing_cost = Entry(my_frame, font = ("Helvetica, 12"))
manufacturing_cost.grid(row=1, column =3, pady=10, padx=10)

category_id = Label(my_frame, text = "Category ID:")
category_id.grid(row=2, column=0, pady=10, padx=10)

category_id = Entry(my_frame, font = ("Helvetica, 12"))
category_id.grid(row = 2, column =1, pady=10, padx=10)

# creating submit and update_butttons for Database Insert and Submit

submit_button = Button(my_frame, text = "Submit", command = submit)
submit_button.grid(row = 3, column =0, pady =10, padx =10)

update_button = Button(my_frame, text = "Update", command = update)
update_button.grid(row=3, column =1, pady=10, padx=10)


# creating a query button for Querying Database

query_button = Button(my_frame, text = "Show Records", command = query)
query_button.grid(row = 4, column =0, columnspan = 2, pady =10, padx =10, ipadx = 130)







 