import time
import csv
import sqlite3, os
from python_dbquery import db_update_mpc
import matplotlib.pyplot as plt
from pathlib import Path

from python_dbquery.db_update_mpc import excel_format

db_file=Path("mydb.db")

if db_file.is_file():

    os.remove("mydb.db")
    time.sleep(10)
else:

    pass

excel_format.extract()
excel_format.to_csv()


class base():

    def __init__(self):
        self.connection_set()

    def connection_set(self):
        self.connection = sqlite3.connect("mydb.db")
        self.cursor = self.connection.cursor()
        query = "create table if not exists servers (hostname TEXT UNIQUE,os TEXT,scope TEXT, type TEXT,ip INT UNIQUE, nat INT, datastore TEXT, application TEXT)"
        self.cursor.execute(query)
        self.connection.commit()

    def connection_cut(self):
        self.connection.close()

    def update(self):
        with open('servers.csv', 'r') as server_table:
            next(server_table)
            #dr = csv.DictReader(server_table, delimiter='\t')  # comma is default delimiter
            dr=csv.reader(server_table)

            query = "insert into servers values(?,?,?,?,?,?,?,?)"

            for i in dr:

                self.cursor.execute(query, (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
                self.connection.commit()


    def change_vp(self):
        query_vm="update servers set type = 'VM' where type = 'V'"
        query_p="update servers set type = 'PHY' where type = 'P'"
        self.cursor.execute(query_vm)
        self.cursor.execute(query_p)
        self.connection.commit()

    def set_null(self):
        query_1="update servers set os = null where os = ''"
        query_2="update servers set scope = null where scope=''"
        query_3="update servers set type = null where type = ''"
        query_4="update servers set nat = null where nat = ''"
        query_5="update servers set datastore = null where datastore = ''"
        query_6="update servers set application = null where application = ''"

        self.cursor.execute(query_1)
        self.cursor.execute(query_2)
        self.cursor.execute(query_3)
        self.cursor.execute(query_4)
        self.cursor.execute(query_5)
        self.cursor.execute(query_6)
        self.connection.commit()

base=base()
base.connection_set()
time.sleep(10)
base.update()
base.change_vp()
base.set_null()


base.connection_cut()

