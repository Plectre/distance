#! usr/bin/python
# -*- coding: utf-8 -*-

import request_api
import csv

exutoires = []
clients = []
output_csv = "output.csv"


def create_first_row_csv(datas):
    file_csv = open(output_csv, "a")
    writer = csv.writer(file_csv, delimiter=";")
    writer.writerow(datas)
    file_csv.close()

def write_csv(col):
    file_csv = open(output_csv, "a")
    writer = csv.writer(file_csv, delimiter=";")
    writer.writerow(col)
    print(col)
    file_csv.close()

def parcours_listes():
    kms = []
    for i in range(0, len(exutoires)):
        print (exutoires[i])
        kms.append(exutoires[i])
        print("Traitement :{0}/{1}".format(i+1, len(exutoires)))
        for j in range(0, len(clients)):
            print("\tTraitement :{0}/{1}".format(j+1, len(clients)))
            try:
                # instantiacion de request
                clients[j].encode()
                request = request_api.Request(exutoires[i], clients[j])
                # Appel fonction de calcul de distance de request
                # renvoie un string
                #result = request.calcul_distance()
                km = request.calcul_distance()
                print(km)
                kms.append(km)
                # sauvegarde du fichier .txt
                #output(result)
                if i + 1 >= len(exutoires) and j+1 >= len(clients):
                    print("Fin des traitements !")
                #print (request)
                #print ("exutoire: {0}, client: {1}".format(exutoires[i], clients[j]))
            except:
                print ("une erreur dans le calcul de la distance !")
                kms.append("--")
                pass
        write_csv(kms)
        kms.clear()

"""Lecture des fichiers exutoires et clients"""
def read_files():
    f_ext = open("exutoires.txt", "r")          # ouverture du fichier exutoires en lecture
    f_clients = open("clients_ville.txt", "r")  # ouverture du fichier clients en lecture
    tmp_ext = f_ext.read()                      # Lecture fichier exutoire.txt
    tmp_clients = f_clients.read()              # Lecture fichier client.txt
    split_ext = tmp_ext.split(",")              # découpage des données selon la virgule dans une variable temporaire
    for ext in split_ext:                       # Parcours de la liste exutoire
        exutoires.append(ext.lower())           # ajout de la valeur dans le tableau exutoire en minuscule
        #print(ext)
    split_client = tmp_clients.split(',')   # découpage des données selon la virgule dans variable temporaire
    for cli in split_client:                # Parcours de la liste client
        clients.append(cli.lower())
        #print (cli)         # ajout de la valeur dans le tableau clients en minuscules
    f_ext.close()
    f_clients.close()
    #create_csv(exutoires)

""" Sortie du resultat dans un fichier"""
def output(result):
    output = open(file_output+".txt", "a")
    output.write(result+"\n")
    output.close()

file_output = input("Nom du fichier en sortie ? ")
read_files()
#print(exutoires)
print(clients)
create_first_row_csv(clients)
parcours_listes()