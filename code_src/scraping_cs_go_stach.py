import requests 

def nombre_pas_possible(url):
	requette = requests.get(url)
	sep1 = requette.text.split("€")
	return(dico_pas_possible[str(len(sep1))])



#Recoder etat pas possible pour renvoyer une liste

def etat_pas_possible(url):
	liste = []
	x = requests.get(url)
	sep = x.text.split("Not Possible")
	for i in range(nombre_pas_possible(url)):
		sep2 = sep[i].split("pull-left")
		sep3 = sep2[-1].split("<")
		sep3 = sep3[0].replace('">"','')
		sep3 = sep3.replace('"','')
		sep3 = sep3.replace('">','')
		sep3 = sep3.replace('>','')
		pas_possible = sep3
		liste.append(etat_dico[pas_possible])
	return(liste)


def recuperation_prix(url):
	"""Permet de recuperer le prix des différents objet en fonction de l'url cs go stash"""
	liste_prix = []
	requette = requests.get(url)
	sep1 = requette.text.split("€")
	cpt_pas_possible = 0
	if ("Not Possible" in requette.text):
		pas_possible = etat_pas_possible(url)
		nb_pas_possible = nombre_pas_possible(url)
		for x in range(5):
			sep2 = sep1[x+6-nb_pas_possible-cpt_pas_possible].split(">")
			if x in pas_possible:
				dico = {"Etat" : etat[x] , "Prix" :  99999999 }
				liste_prix.append(dico)
				cpt_pas_possible += 1 
			else:
				dico = {"Etat" : etat[x] , "Prix" :  float(sep2[-1].replace("\n","").replace("-","0").replace(",",".")) }
				liste_prix.append(dico)
	else:
		for x in range(5):
			sep2 = sep1[x+6].split(">")
			dico = {"Etat" : etat[x] , "Prix" :  float(sep2[-1].replace("\n","").replace("-","0").replace(",",".")) }
			liste_prix.append(dico)
	return(liste_prix)

def recuperation_rarete(url):
	"""Permet de recuperer la rarete des différents objet en fonction de l'url cs go stash"""
	requette = requests.get(url)
	sep1 = requette.text.split("nomargin")
	sep2 = sep1[2].split(">")
	sep3 = sep2[1].split("\n")
	sep4 = sep3[0].split(" ")
	return(sep4[0])


