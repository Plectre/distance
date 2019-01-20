import requests
from save_data import Save
from save_csv import Save_csv

clients = []
exutoires = []
distances = []

""" 
	Fonction se chargeant d'envoyer une requette mapquest avec le <dict> en paramétres
"""
def requette(fr, to):
	KEY = "o7fkcrJwktMPgM4Erg1oN9sGtRS5tvde"
	URL = "http://open.mapquestapi.com/directions/v2/route"
	PARAMS = {'key' : KEY, 'from' : fr, 'to' : to}

	try:
		if fr != "" or to != "": 									# ça ça marche pas !
			r = requests.get(url=URL, params=PARAMS)				# Requette http avec paramétres '&key=<>&to=<>&fr=<>
			data = r.json()											# get json
			statuscode = data['info']['statuscode']
			if statuscode == 0:										# si le serveur est ok
				km = data['route']['distance']						# Extraction des kms
				distances.append(km)								# Add km dans la liste distances
				output = ("{0} => {1} : {2}".format(fr, to, km))	# Envoie vers la sortie
				print(output)
				class_save(output)
			else:													# gestion de l'erreur si statuscode != 0
				print('Erreur {}'.format(statuscode))
				output = ('{0} => {1} : Erreur de requette !'.format(fr, to))
				distances.append('--')								# Add km dans la liste distances
				class_save(output)
		else:
			print('cellule vide')
	except:
			output = ('{0} => {1} : Erreur de requette !'.format(fr, to))
			distances.append('--')
			class_save(output)
			print (output)

	
""" 
	Lecture et formatage du fichier clients
"""
def read_clients():
	clients.append('/')
	f_clients = open("inputs/clients_ville.txt", 'r', encoding='utf8')
	client = f_clients.read()
	split_client = client.split(',')
	for c in split_client:
		clients.append(c)	# ajout dans la liste clients qui sera passé à la requette GET
"""
	Lecture et formatage fichier exutoire
"""
def read_exutoires():
	try:
		f_exutoires = open("inputs/exutoires.txt", 'r', encoding='utf8')
	except IOError:
		print("impossible d'ouvrir le fichier !")
	exutoire = f_exutoires.read()
	split_exutoire = exutoire.split(',')
	for e in split_exutoire:
		exutoires.append(e)	# Ajout dans la liste exutoires qui sera passé à la requette GET

"""
	lecture des listes exutoires et clients
	Appel fonction requette
"""
def exec_requette():
	for i in range(0, len(exutoires)):
		exutoire = exutoires[i]
		distances.append(exutoire)
		for j in range (0, len(clients)):
			client = clients[j]
			requette(exutoire, client)
		csv_save.datas_row(distances)
		distances.clear()

def class_save(output):
	save = Save(output)
	save.save()

read_clients()
read_exutoires()
csv_save = Save_csv("outputs/output.csv")
csv_save.first_row(clients)
exec_requette()
print(distances)