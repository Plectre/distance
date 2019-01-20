#! usr/bin/python
# -*- encoding: utf-8 -*-

"""
Classe qui sauvgarde le fichier sous la forme csv
"""
import csv

class Save_csv():

    def __init__(self, name):
        self.name = name

    def first_row(self, row):
        with open(self.name, "a", encoding='utf8', newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=";")
            # si la cellule est vide on la remove de la liste sinon on l'écrit
            for line in row:
                if line == "":
                    row.remove(line)
            else:
                writer.writerow(row)
        csv_file.close()

    def datas_row(self, data):
        with open (self.name, "a", encoding="utf8", newline="") as csv_data_file:
            writer = csv.writer(csv_data_file, delimiter=";")
            writer.writerow(data)
        csv_data_file.close()

