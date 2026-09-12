import pandas as pd
#import the pandas library and label it as pd
import sqlite3
conn = sqlite3.connect("sales.db")

data = pd.read_csv("Data_engineering/data/sales.csv")
#print(data)
#created a variable called data and used pd to call the pandas library and read the CSV file. 

#data.info()
#data.info() was used to inspect the structure of the data, including the data types and number of non-null values.
#the date column needed to be converted from an object to a datetime data type.
#it was picked up as an object instead of a datetime value.

data["date"] = pd.to_datetime(data["date"])
#selects the date column from data and uses pandas to convert its values to datetime

#data.info()
#data.info() now shows datetime64[ns] for the date column, confirming the conversion was successful.
#print(data.head())
#print(data.head()) was used to print the first 5 rows of the data so we can see how it actually looks.
#this is useful when dealing with big amounts of data as it doesn't output it all to the terminal making a mess.


data["total"] = data["quantity"]*data["price"]
#created a new column called total by multiplying the quantity and price columns together.
#print(data.head())
#shown in terminal with new line of code and it works correctly.
#print(data.head())
#print("The total revenue is ",(data["total"].sum()))
#product_revenue = data.groupby("product")["total"].sum()
#highest_revenue_product = product_revenue.idxmax()

#print(product_revenue)
#print(highest_revenue_product)

#units_sold = data.groupby("product") ["quantity"].sum()
#most_units_sold = units_sold.idxmax()

#date_revenue = data.groupby("date") ["total"].sum()
#highest_date_revenue = date_revenue.idxmax()

#average_order_value = data["total"].mean()
#print(average_order_value.round(2))

#conn.execute("""CREATE TABLE sales (
#    order_id INTEGER PRIMARY KEY,
#    date TEXT,
#    product TEXT,
#    quantity INTEGER,
#    price REAL,
#    total REAL
#);""")

#data.to_sql(
#    name='sales',          # The name of the table in the database
#    con=conn,            # The database connection (Engine or Connection)
#    if_exists='append',   # How to handle the table if it already exists: 'fail', 'replace', or 'append'
#    index=False            # Do not write the DataFrame's index as a column
#)

result = conn.execute("SELECT * FROM sales;")

print(result.fetchall())

