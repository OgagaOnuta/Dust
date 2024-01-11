#!/usr/bin/python3

import sqlite3
import sys


def printDB():
    try:
        result = theCursor.execute("""SELECT ID, FName, LName, Age,
        Address, Salary, HireDate FROM Employees""")

        for row in result:
            print("ID:", row[0])
            print("FName:", row[1])
            print("LName:", row[2])
            print("Age:", row[3])
            print("Address:", row[4])
            print("Salary:", row[5])
            print("HireDate:", row[6])
    except (sqlite3.OperationalError):
        print("The Table Doesn't Exist")
    except (Exception):
        print("Couldn't Retrieve Data from Database")


# Connecting to a database
db_conn = sqlite3.connect("test.db")

print("Database Created")

# A Cursor to traverse your query results
theCursor = db_conn.cursor()

# To execute a SQL command
db_conn.execute("DROP TABLE IF EXISTS Employees")

# To run the command
db_conn.commit()

try:
    db_conn.execute("""CREATE TABLE Employees(
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        FName TEXT NOT NULL,
        LName TEXT NOT NULL,
        Age INTEGER NOT NULL,
        Address TEXT,
        Salary REAL,
        HireDate TEXT)""")

    db_conn.commit()
except (sqlite3.OperationalError):
    print("Table Couldn't Be Created")

print("Table Created")

db_conn.execute("""INSERT INTO Employees
    (FName, LName, Age, Address, Salary, HireDate)
    VALUES ('David', 'Onuta', 26, '123 Main St', 500000, date('now'))""")

db_conn.commit()

print()
printDB()

try:
    db_conn.execute("UPDATE Employees SET Address='121 Main St' WHERE ID=1")
    db_conn.commit()
except (sqlite3.OperationalError):
    print("Table Couldn't Be Updated")

print()
printDB()

'''
try:
    db_conn.execute("DELETE FROM Employees WHERE ID=1")
    db_conn.commit()
except (sqlite3.OperationalError):
    print("Row Couldn't Be Deleted")

print()
printDB()

db_conn.rollback()
'''

try:
    db_conn.execute("""ALTER TABLE Employees ADD COLUMN
        'Image' BLOB DEFAULT NULL""")
    db_conn.commit()
except (sqlite3.OperationalError):
    print("Table Couldn't Be Updated")

theCursor.execute("PRAGMA TABLE_INFO(Employees)")

rowNames = [nameTuple[1] for nameTuple in theCursor.fetchall()]

print(rowNames)
print()

theCursor.execute("SELECT COUNT(*) FROM Employees")
numOfRows = theCursor.fetchall()

print("Total Rows:", numOfRows[0][0])
print()

theCursor.execute("SELECT SQLITE_VERSION()")

print("SQLite Version:", theCursor.fetchone())
print()

with db_conn:
    db_conn.row_factory = sqlite3.Row
    theCursor = db_conn.cursor()
    theCursor.execute("SELECT * FROM Employees")
    rows = theCursor.fetchall()

    for row in rows:
        print("{} {}".format(row["FName"], row["LName"]))

print()

with open("dump.sql", "w") as f:
    for line in db_conn.iterdump():
        f.write("%s\n" % line)

# Closing the connection
db_conn.close()

print("Database Closed")
