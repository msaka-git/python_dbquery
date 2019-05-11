import time
import csv
import sqlite3, os
import matplotlib.pyplot as plt

os.remove('mydb.db')
time.sleep(10)

class base():

    def __init__(self):
        self.connection_set()

    def connection_set(self):
        self.connection = sqlite3.connect("mydb.db")
        self.cursor = self.connection.cursor()
        query = "create table if not exists servers (hostname TEXT UNIQUE,os TEXT,scope TEXT, type TEXT,ip INT UNIQUE, nat INT, datastore TEXT)"
        self.cursor.execute(query)
        self.connection.commit()

    def connection_cut(self):
        self.connection.close()

    def update(self):
        with open('servers.csv', 'r') as server_table:
            next(server_table)
            #dr = csv.DictReader(server_table, delimiter='\t')  # comma is default delimiter
            dr=csv.reader(server_table)

            query = "insert into servers values(?,?,?,?,?,?,?)"

            for i in dr:

                self.cursor.execute(query, (i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
                self.connection.commit()


    def change_vp(self):
        query_vm="update servers set type = 'VM' where type = 'V'"
        query_p="update servers set type = 'PHY' where type = 'P'"
        self.cursor.execute(query_vm)
        self.cursor.execute(query_p)
        self.connection.commit()

base=base()
base.connection_set()
time.sleep(10)
base.update()
base.change_vp()


base.connection_cut()

