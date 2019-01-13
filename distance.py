#! usr/bin/python
# -*- coding: utf-8 -*-

import request_api

exutoires = []
clients = []

def parcours_listes():
    for i in range(0, len(exutoires)):
        print("Traitement :{0}/{1}".format(i+1, len(exutoires)))
        for j in range(0, len(clients)):
            print("\tTraitement :{0}/{1}".format(j+1, len(clients)))
            try:
                request = request_api.Request(exutoires[i], clients[j])
                request = request.calcul_distance()
                output(request)
                if i + 1 >= len(exutoires) and j+1 >= len(clients):
                    print("Fin des traitements !")
                #print (request)
                #print ("exutoire: {0}, client: {1}".format(exutoires[i], clients[j]))
            except:
                #print ("une erreur dans le calcul de la distance !")
                pass
                

"""Lecture des fichiers exutoires et clients"""
def read_files():
    f_ext = open("exutoires.txt", "r")
    f_clients = open("clients.txt", "r")
    tmp_ext = f_ext.read()                  # Lecture fichier exutoire.txt
    tmp_clients = f_clients.read()          # Lecture fichier client.txt
    split_ext = tmp_ext.split(",")          # découpage des données selon la virgule dans variable temporaire
    for ext in split_ext:                   # Parcours de la liste exutoire
        exutoires.append(ext)               # ajout de la valeur dans le tableau exutoire
    split_client = tmp_clients.split(',')   # découpage des données selon la virgule dans variable temporaire
    for cli in split_client:                # Parcours de la liste client
        clients.append(cli)                 # ajout de la valeur dans le tableau clients
    f_ext.close()
    f_clients.close()

""" Sortie du resultat dans un fichier"""
def output(result):
    output = open(file_output+".txt", "a")
    output.write(result+"\n")
    output.close()

file_output = input("Nom du fichier en sortie ? ")
read_files()
#print(exutoires)
#print(clients)
parcours_listes()