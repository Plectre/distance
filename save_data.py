#! usr/bin/python
# -*- coding: utf_8 -*-

import csv

class Save():

    def __init__(self,output):
        self.output = output

    def save(self):
        try:
            f = open('outputs/output.txt', 'a', encoding='utf8')
            f.write(self.output+"\n")
            f.close()
        except EOFError:
            print ("Erreur d'ecriture" + str(EOFError))