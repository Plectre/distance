#! usr/bin/python
# -*- coding :utf-8 -*-
import urllib.request
import json

KEY = "o7fkcrJwktMPgM4Erg1oN9sGtRS5tvde"
URL = "http://open.mapquestapi.com/directions/v2/route"
depart = ""
arrivee = ""
unit = "k"
ambiguite = "ignore" # "check" <> "ignore"

class Request():

    def __init__(self, start, end):
        self.start = start
        self.end = end

    """ Fonction de qui envoie la requette à l API
    de open.mapquestapi.com et reçoie le fichier json """
    def calcul_distance(self):
        with urllib.request.urlopen("{0}?key={1}&from={2}&to={3}&unit={4}&ambiguities={5}".format(URL, KEY, self.start, self.end, unit, ambiguite)) as url:
            data = json.loads(url.read().decode())  
            statuscode = data['info']['statuscode'] # statuscode ok = 0
            if statuscode != 0:
                result = ("{0} ==> {1} : calcul impossible !".format(self.start, self.end))
                #result.encode()
                return "--.-"
            #print ("{0}?key={1}&from={2}&to={3}&unit={4}".format(URL, KEY, depart, arrivee, unit))
            kms = data['route']['distance']
            result = ("{0} ==> {1} : {2} kms".format(self.start, self.end, round(kms, 1)))
            #return result
            return round(kms, 1)