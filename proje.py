import sqlite3
import time
import os
import matplotlib.pyplot as plt


class server():
    def __init__(self, hostname, os, scope, type, ip, nat, datastore):
        self.hostname = hostname
        self.os = os
        self.scope = scope
        self.type = type
        self.ip = ip
        self.nat = nat
        self.datastore = datastore

    def __str__(self):
        return "Hostname: {}\nOS: {}\nScope: {}\nType: {}\nIP: {}\nNat: {}\nDatasotre: {}".format(self.hostname, self.os, self.scope,
                                                                                   self.type, self.ip, self.nat, self.datastore)


class base():

    def __init__(self):
        self.connection_set()

    def connection_set(self):
        self.connection = sqlite3.connect("mydb.db")
        self.cursor = self.connection.cursor()
        query = "create table if not exists servers (hostname TEXT,os TEXT,scope TEXT, type TEXT,ip INT, nat INT, datastore TEXT)"
        self.cursor.execute(query)
        self.connection.commit()

    def connection_cut(self):
        self.connection.close()

    def show_servers(self):
        query = "select * from servers"
        self.cursor.execute(query)
        servers = self.cursor.fetchall()

        if (len(servers) == 0):
            print("Pas de serveur inscrit dans l'inventaire...")

        else:

            for i in servers:
                Servers = server(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
                print(Servers)

    def server_query(self, hostname):

        query = "select * from servers where hostname = ?"
        self.cursor.execute(query, (hostname,))

        servers = self.cursor.fetchall()
        if (len(servers) == 0):
            print("Host n'existe pas.")

        else:
            Servers = server(servers[0][0], servers[0][1], servers[0][2], servers[0][3], servers[0][4], servers[0][5], servers[0][6])
            print(Servers)

    def server_add(self, server):
        query = "insert into servers values(?,?,?,?,?,?,?)"
        self.cursor.execute(query, (server.hostname, server.os, server.scope, server.type, server.ip, server.nat,server.datastore))
        self.connection.commit()

    def server_delete(self, hostname):
        query = "delete from servers where hostname = ?"
        self.cursor.execute(query, (hostname,))
        self.connection.commit()

    def os_change(self, hostname):
        query = "select * from servers where hostname = ?"

        self.cursor.execute(query, (hostname,))

        servers = self.cursor.fetchall()
        if (len(servers) == 0):
            print("Serveur n'existe pas.")

        else:
            os = servers[0][1]

            os = input("Tapez l'OS: ")

            query = "update servers set os = ? where hostname = ?"
            self.cursor.execute(query, (os, hostname))
            self.connection.commit()

    def hostname_change(self, hostname):
        query = "select * from servers where hostname = ?"

        self.cursor.execute(query, (hostname,))
        servers = self.cursor.fetchall()
        if (len(servers) == 0):
            print("Serveur n'existe pas.")

        else:
            name = servers[0][0]

            name = input("Tapez le nouveau hostname: ")
            name = name.upper()

            query = "update servers set hostname = ? where hostname = ?"
            self.cursor.execute(query, (name, hostname))
            self.connection.commit()

    def scope_change(self, hostname):
        query = "select * from servers where hostname = ?"

        self.cursor.execute(query, (hostname,))

        servers = self.cursor.fetchall()
        if (len(servers) == 0):
            print("Serveur n'existe pas.")

        else:
            scope = servers[0][2]

            scope = input("Tapez le nouveau scope: ")
            scope = scope.upper()

            query = "update servers set scope = ? where hostname = ?"
            self.cursor.execute(query, (scope, hostname))
            self.connection.commit()

    def type_change(self, hostname):
        query = "select * from servers where hostname = ?"

        self.cursor.execute(query, (hostname,))

        servers = self.cursor.fetchall()
        if (len(servers) == 0):
            print("Serveur n'existe pas.")

        else:
            type = servers[0][3]

            type = input("Tapez le nouveau Type: ")
            type = type.upper()

            query = "update servers set type = ? where hostname = ?"
            self.cursor.execute(query, (type, hostname))
            self.connection.commit()

    def ip_change(self, hostname):
        query = "select * from servers where hostname = ?"

        self.cursor.execute(query, (hostname,))

        servers = self.cursor.fetchall()
        if (len(servers) == 0):
            print("Serveur n'existe pas.")

        else:
            ip = servers[0][4]

            ip = input("Tapez le nouveau IP: ")

            query = "update servers set ip = ? where hostname = ?"
            self.cursor.execute(query, (ip, hostname))
            self.connection.commit()

    def nat_change(self, hostname):
        query = "select * from servers where hostname = ?"

        self.cursor.execute(query, (hostname,))

        servers = self.cursor.fetchall()
        if (len(servers) == 0):
            print("Serveur n'existe pas.")

        else:
            nat = servers[0][5]

            nat = input("Tapez le nouveau NAT: ")

            query = "update servers set nat = ? where hostname = ?"
            self.cursor.execute(query, (nat, hostname))
            self.connection.commit()

    def ds_change(self, hostname):
        query = "select * from servers where hostname = ?"

        self.cursor.execute(query, (hostname,))

        servers = self.cursor.fetchall()
        if (len(servers) == 0):
            print("Serveur n'existe pas.")

        else:
            datastore = servers[0][6]

            datastore = input("Entrez le nouveau Datastore: ")
            datastore = datastore.upper()

            query = "update servers set datastore = ? where hostname = ?"
            self.cursor.execute(query, (datastore, hostname))
            self.connection.commit()

    def count_servers(self):

        query = "select count (*) from servers"
        self.cursor.execute(query)
        rowcount = self.cursor.fetchone()[0]
        print("Total servers: ", rowcount)

        query2 = "select count (scope) from servers where scope='UO'"
        self.cursor.execute(query2)
        rowcount2 = self.cursor.fetchone()[0]
        print("UO Servers: ", rowcount2)

        query3 = "select count (scope) from servers where scope='HUO'"
        self.cursor.execute(query3)
        rowcount3 = self.cursor.fetchone()[0]
        rowcount3=rowcount3
        print("HUO Servers: ", rowcount3)

        query4 = "select count (type) from servers where type='VM'"
        self.cursor.execute(query4)
        rowcount4 = self.cursor.fetchone()[0]

        phy = int(rowcount - rowcount4)  # PHY servers calcul#
        print("VM Servers: ", rowcount4)
        print("PHY servers: ", phy)
        self.connection.commit()

        labels = (
            'UO={}'.format(rowcount2), 'HUO={}'.format(rowcount3), 'VM={}'.format(rowcount4), 'PHY={}'.format(phy))
        sizes = [rowcount2 / 100, rowcount3 / 100, rowcount4 / 100, phy / 100]
        colors = ['yellow', 'lightblue', 'green', 'red']
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
        plt.title("Au total: {}".format(rowcount))
        plt.suptitle("Repartition des Serveurs")
        plt.savefig('graphique.png')
        #plt.show() # to show the graphique
















