
# Ram Rao Code
# Two Tables Insertion Into Database

#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
import psycopg2
from tkinter import *

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python GUI")

tabControl = ttk.Notebook(win)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text='Tab 1')      # Add the tab
tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text='Tab 2')      # Add second tab 

tabControl.pack(expand=1, fill="both")  # Pack to make visible

# LabelFrame using tab1 and tab2 as the parent

tab1_frame = ttk.LabelFrame(tab1, text=' Manufacturing.Products')
tab1_frame.grid(column=0, row=0, padx=8, pady=4)

tab2_frame = ttk.LabelFrame(tab2, text=' Manufacturing.Categories')
tab2_frame.grid(column=0, row=0, padx=8, pady=4)

# FUNCTIONS FOR MANUFACTURING.PRODUCTS TABLE

# Function for Inserting Records into Table Manufacturing Products

def tab1_submit():
    
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
    
def tab1_query():

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
        
    
    query_label = Label(tab1_frame, text = print_records)
    
    query_label.grid(row =5, column = 0, columnspan = 2)
    
    conn.commit()
    
    conn.close()

# Function for Updating the database

def tab1_update():
   
    conn = psycopg2.connect(database="kineteco",
                       host="localhost",
                       user="postgres",
                       password="Sachin10,dulkar",
                       port="5432")

    cursor = conn.cursor() 
   
    
    cursor.execute ("UPDATE manufacturing.products SET category_id = 2 WHERE category_id = 1")
    
    conn.commit()
    
    conn.close()

# FUNCTIONS FOR TABLE 2, MANUFACTURING.CATEGORIES

def tab2_submit():
    
    conn = psycopg2.connect(database="kineteco",
                            host="localhost",
                            user="postgres",
                            password="Sachin10,dulkar",
                            port="5432")

    cursor = conn.cursor()
        
    # Insert into Table
    # this can be modified as needed so any record in database can be updated
        
    sql = "INSERT INTO manufacturing.categories (category_id, name, market) VALUES (%s, %s, %s)"
    val = (category_id.get(), name.get(), market.get())
    
    cursor.execute(sql, val)
      
    #Commit changes
    
    conn.commit()
    print("Record Inserted")
        
    # Close Connection
    
    conn.close()
        
    #clear the Text Boxes
    category_id.delete(0, END)
    name.delete(0, END)
    market.delete(0, END)
     
    
# Function for Querying the database    
    
def tab2_query():

    conn = psycopg2.connect(database="kineteco",
                        host="localhost",
                        user="postgres",
                        password="Sachin10,dulkar",
                        port="5432")

    cursor = conn.cursor()    

    cursor.execute("SELECT * FROM manufacturing.categories")    
    
    rows = cursor.fetchmany(5)
    
    # loop through results
    
    print_records = ''
    
    for record in rows:
        print_records += str(record) + "\n"
        
    
    query_label = Label(tab2_frame, text = print_records)
    
    query_label.grid(row =5, column = 0, columnspan = 2)
    
    conn.commit()
    
    conn.close()

# Function for Updating the database

def tab2_update():
   
    conn = psycopg2.connect(database="kineteco",
                       host="localhost",
                       user="postgres",
                       password="Sachin10,dulkar",
                       port="5432")

    cursor = conn.cursor() 
   
    
    cursor.execute ("UPDATE manufacturing.categories SET market = 'industrial' WHERE market = 'domestic' ")
    
    conn.commit()
    
    conn.close()


# Tab1 Entry Boxes

product_id = ttk.Label(tab1_frame, text = "Product_ID:")
product_id.grid(row=0, column=0, pady=10, padx=10)

product_id = ttk.Entry(tab1_frame, font = ("Helvetica, 12"))
product_id.grid(row=0, column =1, pady=10, padx=10)

product_name = ttk.Label(tab1_frame, text = "Product_Name:")
product_name.grid(row=1, column=0, pady=10, padx=10)

product_name = ttk.Entry(tab1_frame, font = ("Helvetica, 12"))
product_name.grid(row=1, column =1, pady=10, padx=10)

power = ttk.Label(tab1_frame, text = "Power:")
power.grid(row=0, column=2, pady=10, padx=10)

power = ttk.Entry(tab1_frame, font = ("Helvetica, 12"))
power.grid(row=0, column =3, pady=10, padx=10)

manufacturing_cost = ttk.Label(tab1_frame, text = "Manufacturing Cost:")
manufacturing_cost.grid(row=1, column=2, pady=10, padx=10)

manufacturing_cost = ttk.Entry(tab1_frame, font = ("Helvetica, 12"))
manufacturing_cost.grid(row=1, column =3, pady=10, padx=10)

category_id = ttk.Label(tab1_frame, text = "Category ID:")
category_id.grid(row=2, column=0, pady=10, padx=10)

category_id = ttk.Entry(tab1_frame, font = ("Helvetica, 12"))
category_id.grid(row = 2, column =1, pady=10, padx=10)


# Tab2 Entry Boxes

category_id = ttk.Label(tab2_frame, text = "Category ID:")
category_id.grid(row=0, column=0, pady=10, padx=10)

category_id = ttk.Entry(tab2_frame, font = ("Helvetica, 12"))
category_id.grid(row = 0, column =1, pady=10, padx=10)

name = ttk.Label(tab2_frame, text = "Name:")
name.grid(row=1, column=0, pady=10, padx=10)

name = ttk.Entry(tab2_frame, font = ("Helvetica, 12"))
name.grid(row = 1, column =1, pady=10, padx=10)

market = ttk.Label(tab2_frame, text = "Market:")
market.grid(row=0, column=2, pady=10, padx=10)

market = ttk.Entry(tab2_frame, font = ("Helvetica, 12"))
market.grid(row = 0, column =3, pady=10, padx=10)

# creating submit and update_butttons for Database Insert and Submit, Tab 1

submit_button = ttk.Button(tab1_frame, text = "Submit", command = tab1_submit)
submit_button.grid(row = 3, column =0, pady =10, padx =10)

update_button = ttk.Button(tab1_frame, text = "Update", command = tab1_update)
update_button.grid(row=3, column =1, pady=10, padx=10)

# creating a query button for Querying Database

query_button = ttk.Button(tab1_frame, text = "Show Records", command = tab1_query)
query_button.grid(row = 4, column =0, columnspan = 2, pady =10, padx =10, ipadx = 130)

# creating submit and update_butttons for Database Insert and Submit, Tab 2

submit_button = ttk.Button(tab2_frame, text = "Submit", command = tab2_submit)
submit_button.grid(row = 3, column =0, pady =10, padx =10)

update_button = ttk.Button(tab2_frame, text = "Update", command = tab2_update)
update_button.grid(row=3, column =1, pady=10, padx=10)


# creating a query button for Querying Database

query_button = ttk.Button(tab2_frame, text = "Show Records", command = tab2_query)
query_button.grid(row = 4, column =0, columnspan = 2, pady =10, padx =10, ipadx = 130)



