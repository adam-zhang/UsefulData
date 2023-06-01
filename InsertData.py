#!/usr/bin/python3
import sys
import sqlite3

def insertToDatabase(number, text):
   connection = sqlite3.connect("data.db")
   cursor = connection.cursor()
   sql = "insert into IdentityCard(ID, code)values(" + str(number) + ",\"" + text + "\")"
   print(sql)
   cursor.execute(sql)
   connection.commit()
   connection.close()



def readFile(fileName):
    with open(fileName) as file:
        line = file.readline()
        count = 0
        while line:
            line = file.readline()
            splited = line.split()
            if len(splited) != 0:
                insertToDatabase(splited[0], splited[1])

def initDatabase():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("create table if not exists IdentityCard("
            "ID integer primary key autoincrement,"
            "code char(6),"
            "region nvarchar(50) "
            ")"
            )
    connection.close()
    

def main():
    initDatabase()
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], " file_name")
        return
    readFile(sys.argv[1])

if __name__ =="__main__":
    main()
