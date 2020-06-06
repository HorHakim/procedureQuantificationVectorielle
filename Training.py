#include:utf-8
"""
Author : Horairy Hakim

"""

from generatorDictionnary import *
from Algorithme import *
import pickle

def training(tailleBloc, numberIteration):
	batch = creatorBatch(tailleBloc)
	print("création du batch réussi, début de l'entrainement")
	dictionnaryPrototype = lbg(batch, numberIteration)
	print("Entrainement Réussi")
	del dictionnaryPrototype["dictionnaryFlattenedBlocsImage"]
	
	for key, value in dictionnaryPrototype.items() : 
		if key == "metaData":
			pass
		else:
			dictionnaryPrototype[key] = dictionnaryPrototype[key][0]
	print("Mise en forme du dictionnaire de Prototype réussie")
	
	with open('DictionnairePrototype', 'wb') as fichier:
		mon_pickler = pickle.Pickler(fichier)
		mon_pickler.dump(dictionnaryPrototype)
	print("Dictionnaire de prototype sauvegardé correctement")

	return None