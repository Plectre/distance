import requests
from save_data import Save

clients = []
exutoires = []

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
				output = ("{0} => {1} : {2}".format(fr, to, km))	# Envoie vers la sortie
				print(output)
				class_save(output)
			else:													# gzstion de l'erreur si statuscode != 0
				print('Erreur {}'.format(statuscode))
				output = ('{0} => {1} : Erreur de requette !'.format(fr, to))	
				class_save(output)
		else:
			print('cellule vide')
	except:
			output = ('{0} => {1} : Erreur de requette !'.format(fr, to))
			class_save(output)
			print (output)
	
""" 
	Lecture et formatage du fichier clients
"""
def read_clients():
	f_clients = open("inputs/clients_ville.txt", 'r', encoding='utf8')
	client = f_clients.read()
	split_client = client.split(',')
	for c in split_client:
		clients.append(c)	# ajout dans la liste clients qui sera passé à la requette GET

"""
	Lecture et formatage fichier exutoire
"""
def read_exutoires():
	f_exutoires = open("inputs/exutoires.txt", 'r', encoding='utf8')
	exutoire = f_exutoires.read()
	split_exutoire = exutoire.split(',')
	for e in split_exutoire:
		exutoires.append(e)	# Ajout dans la liste exutoire qui sera passé à la requette GET

"""
	lecture des listes exutoires et clients
	Appel fonction requette
"""
def exec_requette():
	for i in range(0, len(exutoires)):
		exutoire = exutoires[i]
	for j in range (0, len(clients)):
		client = clients[j]
		if exutoire != "" and client != "":
			requette(exutoire, client)
		else:
			print("! Au moins,une des entrées est vide, pas de requette GET !")

# def save(output):
# 	try:
# 		f = open('output.txt', 'a', encoding='utf8')
# 		f.write(output+"\n")
# 		f.close()
# 	except:
# 		print ("Erreur d'ecriture")

def class_save(output):
	save = Save(output)
	save.save()

read_clients()
read_exutoires()
exec_requette()

