from scraping_cs_go_stach import *

etats = ["Factory new","Minimal Wear","Field-tested","Well-Worn","Battle-Scarred"]
rarete = ["Mil-Spec","Restricted","Classified","Covert"]
dico_rarete = {"Mil-Spec" : 0, 'Restricted' : 1, "Classified" : 2,"Covert" : 3}

chroma2_case = ['https://csgostash.com/skin/566/MP7-Armor-Core',"https://csgostash.com/skin/563/Negev-Man-o-war",
"https://csgostash.com/skin/562/Sawed-Off-Origami"
,"https://csgostash.com/skin/564/P250-Valence","https://csgostash.com/skin/565/Desert-Eagle-Bronze-Deco"
,"https://csgostash.com/skin/567/AK-47-Elite-Build","https://csgostash.com/skin/558/UMP-45-Grand-Prix","https://csgostash.com/skin/559/CZ75-Auto-Pole-Position"
,"https://csgostash.com/skin/560/MAG-7-Heat", "https://csgostash.com/skin/561/AWP-Worm-God",
"https://csgostash.com/skin/557/Five-SeveN-Monkey-Business","https://csgostash.com/skin/556/Galil-AR-Eco"
,"https://csgostash.com/skin/555/FAMAS-Djinn","https://csgostash.com/skin/554/M4A1-S-Hyper-Beast",
"https://csgostash.com/skin/553/MAC-10-Neon-Rider"]

snake_bite_case = ['https://csgostash.com/skin/1376/USP-S-The-Traitor','https://csgostash.com/skin/1377/M4A4-In-Living-Color','https://csgostash.com/skin/1375/Galil-AR-Chromatic-Aberration'
,'https://csgostash.com/skin/1373/MP9-Food-Chain','https://csgostash.com/skin/1374/XM1014-XOXO','https://csgostash.com/skin/1368/AK-47-Slate','https://csgostash.com/skin/1372/Desert-Eagle-Trigger-Discipline',
"https://csgostash.com/skin/1371/MAC-10-Button-Masher","https://csgostash.com/skin/1370/Negev-dev-texture","https://csgostash.com/skin/1369/P250-Cyber-Shell",
"https://csgostash.com/skin/1361/Glock-18-Clear-Polymer","https://csgostash.com/skin/1367/CZ75-Auto-Circaetus","https://csgostash.com/skin/1364/R8-Revolver-Junk-Yard",
"https://csgostash.com/skin/1363/SG-553-Heavy-Metal","https://csgostash.com/skin/1362/M249-OSIPR","https://csgostash.com/skin/1366/Nova-Windblown",
"https://csgostash.com/skin/1365/UMP-45-Oscillator"]


chroma3_case = ["https://csgostash.com/skin/742/M4A1-S-Chanticos-Fire","https://csgostash.com/skin/736/PP-Bizon-Judgement-of-Anubis",
"https://csgostash.com/skin/745/P250-Asiimov","https://csgostash.com/skin/750/UMP-45-Primal-Saber",
"https://csgostash.com/skin/735/AUG-Fleet-Flock","https://csgostash.com/skin/748/SSG-08-Ghost-Crusader","https://csgostash.com/skin/751/XM1014-Black-Tie",
"https://csgostash.com/skin/749/Tec-9-Re-Entry","https://csgostash.com/skin/740/Galil-AR-Firefight","https://csgostash.com/skin/737/CZ75-Auto-Red-Astor",
"https://csgostash.com/skin/743/MP9-Bioleak","https://csgostash.com/skin/738/Dual-Berettas-Ventilators","https://csgostash.com/skin/747/SG-553-Atlas",
"https://csgostash.com/skin/744/P2000-Oceanic","https://csgostash.com/skin/741/M249-Spectre","https://csgostash.com/skin/739/G3SG1-Orange-Crash",
"https://csgostash.com/skin/746/Sawed-Off-Fubar"]

recoil_case = ['https://csgostash.com/skin/1532/USP-S-Printstream',"https://csgostash.com/skin/1533/AWP-Chromatic-Aberration",
"https://csgostash.com/skin/1529/AK-47-Ice-Coaled","https://csgostash.com/skin/1531/Sawed-Off-Kiss%E2%99%A5Love",
"https://csgostash.com/skin/1530/P250-Visions","https://csgostash.com/skin/1528/Dual-Berettas-Flora-Carnivora","https://csgostash.com/skin/1526/SG-553-Dragon-Tech",
"https://csgostash.com/skin/1527/P90-Vent-Rush","https://csgostash.com/skin/1525/M249-Downtown","https://csgostash.com/skin/1524/R8-Revolver-Crazy-8"
,"https://csgostash.com/skin/1519/M4A4-Poly-Mag","https://csgostash.com/skin/1523/Glock-18-Winterized","https://csgostash.com/skin/1517/FAMAS-Meow-36",
"https://csgostash.com/skin/1520/MAC-10-Monkeyflage","https://csgostash.com/skin/1522/UMP-45-Roadblock","https://csgostash.com/skin/1521/Negev-Drop-Me",
"https://csgostash.com/skin/1518/Galil-AR-Destroyer"]


def creation_dictionnaire_caractéristic(collection):
	"""Create a dictionary with all the characteristics of the collection (number of weapons and number in the different rarities)"""
	somme_mil_spec = 0
	somme_restricted = 0 
	somme_classified = 0
	somme_covert = 0
	for url in collection:
		if recuperation_rarete(url) == "Mil-Spec":
			somme_mil_spec += 1 
		if recuperation_rarete(url) == "Restricted":
			somme_restricted += 1 
		if recuperation_rarete(url) == "Classified":
			somme_classified += 1
		if recuperation_rarete(url) == "Covert":
			somme_covert += 1 
	return({"Taille_collection" : len(collection),"Mil-Spec"  : somme_mil_spec,"Restricted" : somme_restricted, "Classified" : somme_classified , "Covert" : somme_covert})

def creation_dictionnaire(collection):
	"""Create a dictionary with all the data related to the collection"""
	liste_dico = []
	liste_dico.append(creation_dictionnaire_caractéristic(chroma2_case))
	for url in collection:
		dico = {"Nom" : url.split('/')[-1], "Rarete" : recuperation_rarete(url), "Prix" : recuperation_prix(url)  }
		liste_dico.append(dico)
	return(liste_dico)



def prix_minimum_rarete_etat(dico_collection):
	"""Gives the minimum price according to scarcity and condition"""
	dictionnaire = {}
	minimum = 100000
	indice_min = 0
	for rare in rarete:
		for i in range(len(etats)):
			for k in range(len(dico_collection)-1):
				if (dico_collection[k+1]["Prix"][i]['Prix'] < minimum) and (dico_collection[k+1]["Rarete"] == rare):
					minimum = dico_collection[k+1]["Prix"][i]['Prix'] 
					indice_min = k 
			dictionnaire[rare+" | "+etats[i]] = minimum*10
			minimum = 100000
	return(dictionnaire)


def prix_moyen_rarete_etat(dico_collection):
	"""Gives the average price according to rarity and condition (not taken into account if does not exist) """
	dictionnaire = {}
	somme = 0
	cpt_somme = 0
	for rare in rarete:
		for i in range(len(etats)):
			for k in range(len(dico_collection)-1):
				if (dico_collection[k+1]["Rarete"] == rare):
					if dico_collection[k+1]["Prix"][i]['Prix'] != 99999999:
						somme += dico_collection[k+1]["Prix"][i]['Prix']
						cpt_somme +=1

			dictionnaire[rare+" | "+etats[i]] = somme/cpt_somme
			somme = 0
			cpt_somme = 0
	return(dictionnaire)

def esperance_de_gain(dico_collection):
	"""Gives the earnings expectancy for each crate"""
	dico = {}
	dico_mini = prix_minimum_rarete_etat(dico_collection)
	dico_moy = prix_moyen_rarete_etat(dico_collection)
	for i in range(len(rarete)-1):
		for j in range(len(etats)):
			dico[rarete[i+1] + ' | '+ etats[j]] = dico_moy[rarete[i+1] + ' | ' + etats[j]]  - dico_mini[rarete[i] + ' | ' + etats[j]]
			if (dico_moy[rarete[i+1] + ' | ' + etats[j]]  - dico_mini[rarete[i] + ' | ' + etats[j]]) > 0:
				#print if a trade is worth it
				print(rarete[i+1] + ' | ' + etats[j])
	return(dico)
	


dico_colection = creation_dictionnaire(recoil_case)

print(esperance_de_gain(dico_colection))