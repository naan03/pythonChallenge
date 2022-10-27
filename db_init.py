#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="127.0.0.1", port="5432")
print ("Opened database successfully")

def create_table():
    cur = conn.cursor()
    cur.execute('''CREATE TABLE FILES
           (ID INT PRIMARY KEY     NOT NULL,
           FILE_NAME           TEXT    NOT NULL,
           FILE_DATA           TEXT    );''')
    print ("Table created successfully")

def insert_data():
    cur = conn.cursor()

    cur.execute("INSERT INTO FILES (ID,FILE_NAME,FILE_DATA) \
          VALUES (1, '2022-10-26-10_00_00.csv', 'California')");

    cur.execute("INSERT INTO FILES (ID,FILE_NAME,FILE_DATA) \
          VALUES (2, '2022-10-26-10_01_01.csv', 'Texas')");

    print ("Records created successfully")

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()
    insert_data()
