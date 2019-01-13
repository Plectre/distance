#! usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib.request

KEY = "o7fkcrJwktMPgM4Erg1oN9sGtRS5tvde"
URL = "http://open.mapquestapi.com/directions/v2/route"
depart = ""
arrivee = ""
unit = "k"
exutoires = []
clients = []

""" Fonction de qui envoie la requette à l API
    de open.mapquestapi.com et reçoie le fichier json """
def calcul_distance(start, stop):
    with urllib.request.urlopen("{0}?key={1}&from={2}&to={3}&unit={4}".format(URL, KEY, start, stop, unit)) as url:
        data = json.loads(url.read().decode())  
        statuscode = data['info']['statuscode'] # stauscode ok = 0
        if statuscode != 0:
            result = ("{0} ==> {1} : calcul impossible !".format(start, stop))
            output(result)
            return
        #print ("{0}?key={1}&from={2}&to={3}&unit={4}".format(URL, KEY, depart, arrivee, unit))
        kms = data['route']['distance']
        result = ("{0} ==> {1} : {2} kms".format(start, stop, round(kms, 1)))
        output(result)

def parcours_listes():
    for i in range(0, len(exutoires)):
        for j in range(0, len(clients)):
            try:
                calcul_distance(exutoires[i], clients[j])
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

""" Sortie du resultat """
def output(result):
    output = open(file_output+".txt", "a")
    output.write(result+"\n")
    output.close()

file_output = input("Nom du fichier en sortie ? ")
read_files()
#print(exutoires)
#print(clients)
parcours_listes()