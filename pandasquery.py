"""
Write a pandas function that queries a database by extracting data from a table and returning the result as a pandas dataframe.
Start by creating a connection to the database using the sqlite3 library. Then, write a function that takes a SQL query as an argument and returns a pandas dataframe of the result.
Create a database using the following data:
"""
import sqlite3
import pandas as pd

def create_db():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE stocks (
            date text,
            trans text,
            symbol text,
            qty real,
            price real
        )
    ''')
    conn.commit()
    conn.close()

def insert_data(date, trans, symbol, qty, price):
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("INSERT INTO stocks VALUES (?, ?, ?, ?, ?)", (date, trans, symbol, qty, price))
    conn.commit()
    conn.close()

def query_db(query):
    conn = sqlite3.connect('mydatabase.db')
    df = pd.read_sql_query(query, conn)
    conn.close()

    return df

if __name__ == "__main__":
    create_db()
    insert_data('2020-01-01', 'BUY', 'AAPL', 100, 300)
    insert_data('2020-01-02', 'SELL', 'AAPL', 50, 310)
    insert_data('2020-01-03', 'BUY', 'GOOGL', 200, 1200)
    insert_data('2020-01-04', 'SELL', 'GOOGL', 100, 1300)
    print(query_db('SELECT * FROM stocks'))
    print(query_db('SELECT * FROM stocks WHERE symbol = "AAPL"'))