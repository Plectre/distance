#! usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib.request

KEY = "o7fkcrJwktMPgM4Erg1oN9sGtRS5tvde"
URL = "http://open.mapquestapi.com/directions/v2/route"
depart = ""
arrivee = ""
unit = "k"
exutoires = ['begles', 'libournes']
clients = ["nice", "paris"]

""" Fonction de qui envoie la requette à l API
    de open.mapquestapi.com et reçoie le fichier json """
def calcul_distance(start, stop):
    with urllib.request.urlopen("{0}?key={1}&from={2}&to={3}&unit={4}".format(URL, KEY, start, stop, unit)) as url:
        data = json.loads(url.read().decode())
    #print ("{0}?key={1}&from={2}&to={3}&unit={4}".format(URL, KEY, depart, arrivee, unit))
    kms = data['route']['distance']
    print ("{0} ==> {1} : {2} kms".format(start, stop, round(kms, 1)))

def parcours_listes():
    for i in range(0, len(exutoires)):
        for j in range(0, len(clients)):
            try:
                calcul_distance(exutoires[i], clients[j])
                #print ("exutoire: {0}, client: {1}".format(exutoires[i], clients[j]))
            except:
                print ("une erreur dans le calcul de la distance !")
                

#parcours_listes()
def read_files():
    f_ext = open("exutoires.txt", "r")
    f_clients = open("clients.txt", "r")
    tmp_ext = f_ext.read()
    tmp_clients =f_clients.read()
    exutoires.append(str(tmp_ext))
    clients.append(str(tmp_clients))
    f_ext.close()
    f_clients.close()

#read_files()
print(exutoires)
print(clients)
read_files()
parcours_listes()