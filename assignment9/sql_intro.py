# import pandas as pd
import sqlite3
import os

os.makedirs("../db", exist_ok=True)

try: 
    # connecting to the database
    conn = sqlite3.connect("../db/magazines.db")
    # validates foregin key
    conn.execute("PRAGMA foreign_keys = 1")
    #cursor to execute SQL
    cursor = conn.cursor()
    #publisher table
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS publishers (
                   publishers_id INTEGER PRIMARY KEY, 
                   name TEXT NOT NULL UNIQUE,
                   publishers_type TEXT NOT NULL
    );
    """)

    #magazines table
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS magazines (
                   magazines_id INTEGER PRIMARY KEY, 
                   name TEXT NOT NULL UNIQUE,
                   category TEXT NOT NULL,
                   publishers_id INTEGER NOT NULL,
                   FOREIGN KEY (publishers_id) REFERENCES publishers (publishers_id)
    );
    """)

    # subscribers table
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS subscribers (
                   subscribers_id INTEGER PRIMARY KEY, 
                   name TEXT NOT NULL,
                   address TEXT NOT NULL 
    );
    """)
    # subscrption table(join table)
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS subscriptions ( 
                    subscriptions_id INTEGER PRIMARY KEY,
                    magazines_id INTEGER NOT NULL,
                    subscribers_id INTEGER NOT NULL,
                    expiration_date TEXT NOT NULL,
                    UNIQUE(subscribers_id, magazines_id),
                    FOREIGN KEY (subscribers_id) REFERENCES subscribers(subscribers_id),
                    FOREIGN KEY (magazines_id) REFERENCES magazines(magazines_id)
    );
    """)

# add publisher
    def add_publishers(cursor, name, publishers_type):
        try:
        # try insert publisher
            cursor.execute("INSERT INTO publishers (name, publishers_type) VALUES (?, ?)",(name, publishers_type)
        )
        except sqlite3.IntegrityError:
            print(f"publisher  '{name}' already exist.")
        # prevents dups publisher names
            pass
# add magazine
    def add_magazines(cursor, name, category, publishers_id):
        try:
            cursor.execute("INSERT INTO magazines (name, category, publishers_id) VALUES(?, ?, ?)", (name, category, publishers_id)
        )
        except sqlite3.IntegrityError:
            print(f"Magazine '{name}' already exists.")
        # prevents dups
            pass
# add subscribrs
    def add_subscribers(cursor, name, address):
        # checking the dups
        cursor.execute( "SELECT * FROM subscribers WHERE name = ? AND address = ?", (name, address)
                    )
        if cursor.fetchone():
            # if exists does nothing
            return  
        try:
            cursor.execute("INSERT INTO subscribers (name, address) VALUEs(?, ?)", (name, address)
            )
        except sqlite3.IntegrityError:
            pass
# add subscription
    def add_subscriptions(cursor, subscribers_id, magazines_id, expiration_date):
        #checking for subs if they already have the magz
        cursor.execute("SELECT * FROM subscriptions WHERE subscribers_id = ? AND magazines_id = ?", (subscribers_id, magazines_id)
                    )
        if cursor.fetchone():
            return
        try:
            cursor.execute("INSERT INTO subscriptions (subscribers_id, magazines_id, expiration_date) VALUES (?, ?, ?)", (subscribers_id, magazines_id, expiration_date)
                        )   
        except sqlite3.IntegrityError:
            pass    

# 
# publishers
    add_publishers(cursor, "Bay Media", "Magazine")
    add_publishers(cursor, "Today Media", "Online")
    add_publishers(cursor, "Business Insider", "Digital")

    #magazines
    add_magazines(cursor, "Bay Monthly", "Life Style", 1)
    add_magazines(cursor, "Business Daily", "Business", 3)
    add_magazines(cursor, "Techo", "Technology", 2)

    #subscribers
    add_subscribers(cursor, "Simran Smith", "123 Oak St")
    add_subscribers(cursor, "Julia Park", "456 Sac Dr")
    add_subscribers(cursor, "Mark Rai", "789 Pine Rd")

    #subscriptions 
    add_subscriptions(cursor, 1, 1, "2026-01-01")  
    add_subscriptions(cursor, 2, 2, "2026-05-11")  
    add_subscriptions(cursor, 3, 3, "2026-12-03")  

    # query, retrieve info from subscribers 
    cursor.execute("SELECT * FROM subscribers;")
    subscribers = cursor.fetchall()
    for subscriber in subscribers:
        print(subscriber)
        
    # retrieve all mgz by name
    cursor.execute("SELECT * FROM magazines ORDER BY name;")
    magazines = cursor.fetchall()
    for magazine in magazines:
        print(magazine)
        
    # find publisher using JOIN
    publisher_name = "Today Media"
    cursor.execute(""" 
        SELECT m.magazines_id, m.name, m.category, p.name
        FROM magazines m
        JOIN publishers p
        ON m.publishers_id = p.publishers_id
        WHERE p.name = ?          
    """, (publisher_name,))
    magazines_for_publisher = cursor.fetchall()
    for magz in magazines_for_publisher:
        print(magz)

    conn.commit()
    
except sqlite3.Error as e:
    # handles any SQL error
    print("An error occured:", e)

# closing the connection
finally:
    if conn:
        conn.close()

# databse file created
if os.path.exists("../db/magazines.db"):
        print("Database file created successfully!")


