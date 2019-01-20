from proje import *
from xlsxwriter.workbook import Workbook
import os

print("""**************************************

BIENVENUE A L'OUTIL D'INTERROGATION SERVEURS

Operations;

1-Lister les serveurs

2-Interroger un serveur

3-Ajoutez serveur

4-Supprimer serveur

5-Extraire dans Excel

6-Mettre a jour le serveur

7-Resume


pour quitter appuyez sur 'q'.

**************************************""")

base = base()


def style_excel():
    workbook = Workbook('inventaire.xlsx')
    worksheet1 = workbook.add_worksheet("Liste des Serveurs")
    worksheet1.set_column('A:F', 30)
    bold = workbook.add_format({'bold': True})

    style_head = workbook.add_format(
        {
            "bg_color": "#b7b795",
            "bold": True,
            "border": 1,
            "border_color": "#000000"

        }

    )

    worksheet1.write('A1', 'Hostname', style_head)
    worksheet1.write('B1', 'OS', style_head)
    worksheet1.write('C1', 'Scope', style_head)
    worksheet1.write('D1', 'PHY/VM', style_head)
    worksheet1.write('E1', 'Ip', style_head)
    worksheet1.write('F1', 'Nat', style_head)

    conn = sqlite3.connect('mydb')
    c = conn.cursor()
    c.execute("select * from servers")
    mysel = c.execute("select * from servers ")

    style1 = workbook.add_format(
        {
            "bg_color": "#b3b3ff",
            "border": 1,
            "border_color": "#000000"

        }

    )

    style2 = workbook.add_format(
        {
            "bg_color": "#ffc2b3",
            "border": 1,
            "border_color": "#000000"

        }

    )

    for i, row in enumerate(mysel, 1):

        for j, value in enumerate(row):

            if (i % 2 == 0):
                worksheet1.write(i, j, value, style1)
            else:
                worksheet1.write(i, j, value, style2)

    worksheet2 = workbook.add_worksheet("graphique")
    worksheet2.set_column('A:A', 30)
    worksheet2.write('A2', 'Vue statistique:')
    worksheet2.insert_image('B2', 'graphique.png')


    workbook.close()


while True:
    operation = input("Choissez l'operation: ")

    if (operation == "q"):
        print("Operation terminee...")
        print("A la prochaine...")
        exit(0)

    elif (operation == "1"):
        base.show_servers()

    elif (operation == "2"):
        hostname = input("Tapez le serveur souhaite: ?")
        hostname = hostname.upper()
        print("En cours...")
        time.sleep(2)

        base.server_query(hostname)

    elif (operation == "3"):
        hostname = input("Hostname: ")
        hostname = hostname.upper()
        os = input("OS: ")
        scope = input("Scope(uo/huo): ")
        scope = scope.upper()
        type = input("Type: ")
        type = type.upper()
        ip = input("IP: ")
        nat = input("Nat: ")

        new_server = server(hostname, os, scope, type, ip, nat)
        print("Ajout du serveur en cours...")
        time.sleep(2)
        base.server_add(new_server)

        print("Serveur ajoute...")


    elif (operation == "4"):
        hostname = input("Serveur a supprimer: ")
        hostname = hostname.upper()
        reponse = input("Etes-vous sur? (o/n): ")
        if (reponse == "o"):
            print("Supression en cours...")
            time.sleep(2)
            base.server_delete(hostname)
            print("Serveur supprime...")

    elif (operation == "5"):
        base.count_servers()
        style_excel()
        print("Fichier enregistre.")
        time.sleep(5)
        print("Fichier se trouve dans: {}".format(os.getcwd()))
        filepath = "graphique.png"

        if os.path.exists(filepath):
            os.remove(filepath)
        else:
            exit(0)
        break

    elif (operation == "7"):
        base.count_servers()

    elif (operation == "6"):
        print("\n*****\n"
              "Choisissez la modification a faire"
              "\n----------------------------------\n"
              "1- Modifier hostname\n"
              "2- Modifier OS\n"
              "3- Modifier Scope\n"
              "4- Modifier Type\n"
              "5- Modifier Ip\n"
              "6- Modifier Nat\n"
              "*****")

        reponse_s = int(input("Faites votre choix (1/2/3/4/5/6): "))

        if (reponse_s == 1):
            hostname = input("Sur quel serveur voulez-vous modifier Hostname: ")
            hostname = hostname.upper()
            print("Modification en cours...")
            time.sleep(2)

            base.hostname_change(hostname)
            print("Hostname a ete modifie.")

        elif (reponse_s == 2):
            hostname = input("Sur quel serveur voulez-vous modifier l'OS: ")
            hostname = hostname.upper()
            print("Modification en cours...")
            time.sleep(2)
            base.os_change(hostname)
            print("OS a ete mis a jour.")

        elif (reponse_s == 3):
            hostname = input("Sur quel serveur voulez-vous modifier Scope: ")
            hostname = hostname.upper()
            print("Modification en cours...")
            time.sleep(2)
            base.scope_change(hostname)
            print("Scope a ete modifie.")

        elif (reponse_s == 4):
            hostname = input("Sur quel serveur voulez-vous modifier Type: ")
            hostname = hostname.upper()
            print("Modification en cours...")
            time.sleep(2)
            base.type_change(hostname)
            print("Type a ete modifie.")

        elif (reponse_s == 5):
            hostname = input("Sur quel serveur voulez-vous modifier IP: ")
            hostname = hostname.upper()
            print("Modification en cours...")
            time.sleep(2)
            base.ip_change(hostname)
            print("IP a ete modifie.")

        elif (reponse_s == 6):
            hostname = input("Sur quel serveur voulez-vous modifier NAT: ")
            hostname = hostname.upper()
            print("Modification en cours...")
            time.sleep(2)
            base.nat_change(hostname)
            print("NAT a ete modifie.")


    else:
        print("Operation invalide.")

base.connection_cut()
print("DB Connection closed")




