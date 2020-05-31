#include:utf-8
"""
Author : Cécilia Hakim Zacharie

"""

import numpy as np


def calculGravityCenterBloc(dictionnary):
	"""En cours de construction
		Fonction permettant de calculer le centre de gravité des blocs flattened de l'image."""
	tailleBloc = dictionnary["metaData"]["tailleBloc"] 
	rgb = dictionnary["metaData"]["rgb"] 
	tailleGravityCenterBloc = tailleBloc**2
	gravityCenterBloc = np.zeros((tailleGravityCenterBloc))	

	if dictionnary["metaData"]["typeDictionnary"] == "DictionnaryFlattenedBlocsImage":
		numberLinesBlocs = dictionnary["metaData"]["numberLinesBlocs"]
		numberColumnsBlocs = dictionnary["metaData"]["numberColumnsBlocs"]
		numberTotalBlocs = numberLinesBlocs*numberColumnsBlocs
		
		for i in range(numberLinesBlocs):
			for j in range(numberColumnsBlocs):
				indexBloc = str(int(i/tailleBloc)) + "," +  str(int(j/tailleBloc))
				gravityCenterBloc += dictionnary[indexBloc]
		
		gravityCenterBloc /= numberTotalBlocs
		return gravityCenterBloc
	
	elif dictionnary["metaData"]["typeDictionnary"] == "dictionnaryPrototype" and dictionnary["metaData"]["UpToDateCentresOfGravity"] == False:
		numberPrototypes = dictionnary["metaData"]["numberPrototypes"]
		for i in range(numberPrototypes):
			indexPrototype = "Prototype" + str(i)
			for indexBloc in dictionnary[indexPrototype][1] :
				gravityCenterBloc += dictionnary["dictionnaryFlattenedBlocsImage"][indexBloc]
			numberTotalBlocs = len(dictionnary[indexPrototype][1])
			gravityCenterBloc /= numberTotalBlocs
			dictionnary[indexPrototype][0] = gravityCenterBloc
			gravityCenterBloc = np.zeros((tailleGravityCenterBloc))	
		 
		dictionnary["metaData"]["UpToDateCentresOfGravity"] == True
		print("Les centres de gravité sont maintenant à jour")
		return dictionnary
	else : 
		print("error")
		return None



def splitVector(gravityCenterBloc, tailleBloc, rgb=False):
	epsilonShape = gravityCenterBloc.shape
	epsilon = np.random.random_sample(epsilonShape)
	
	gravityCenterBlocPlusEpsilon = gravityCenterBloc + epsilon
	gravityCenterBlocMoinsEpsilon = gravityCenterBloc - epsilon
	
	return gravityCenterBlocPlusEpsilon, gravityCenterBlocMoinsEpsilon


def createDictionnaryPrototype(dictionnaryFlattenedBlocsImage):
	if dictionnaryFlattenedBlocsImage["metaData"]["typeDictionnary"] == "DictionnaryFlattenedBlocsImage" :	
		dictionnaryPrototype = dict()
		
		dictionnaryPrototype["metaData"] = dict()
		dictionnaryPrototype["metaData"]["typeDictionnary"] = "dictionnaryPrototype"
		dictionnaryPrototype["metaData"]["tailleBloc"] = dictionnaryFlattenedBlocsImage["metaData"]["tailleBloc"]
		dictionnaryPrototype["metaData"]["rgb"] = dictionnaryFlattenedBlocsImage["metaData"]["rgb"]
		dictionnaryPrototype["metaData"]["numberLinesBlocs"]= dictionnaryFlattenedBlocsImage["metaData"]["numberLinesBlocs"]
		dictionnaryPrototype["metaData"]["numberColumnsBlocs"] = dictionnaryFlattenedBlocsImage["metaData"]["numberColumnsBlocs"]
		dictionnaryPrototype["metaData"]["numberPrototypes"] = 2
		dictionnaryPrototype["metaData"]["UpToDateCentresOfGravity"] = False

		dictionnaryPrototype["dictionnaryFlattenedBlocsImage"] = dictionnaryFlattenedBlocsImage
		
		numberLinesBlocs = dictionnaryPrototype["metaData"]["numberLinesBlocs"]
		numberColumnsBlocs = dictionnaryPrototype["metaData"]["numberColumnsBlocs"]
		tailleBloc = dictionnaryPrototype["metaData"]["tailleBloc"]
		rgb = dictionnaryPrototype["metaData"]["rgb"]

		gravityCenterBloc = calculGravityCenterBloc(dictionnaryFlattenedBlocsImage)
		gravityCenterBlocPlus, gravityCenterBlocMoins = splitVector(gravityCenterBloc, tailleBloc)

		dictionnaryPrototype["Prototype0"] = [gravityCenterBlocMoins, []]
		dictionnaryPrototype["Prototype1"] = [gravityCenterBlocPlus, []]
		

		for i in range(numberLinesBlocs):
			for j in range(numberColumnsBlocs):
				indexBloc = str(int(i)) + "," +  str(int(j))
				distEpsilonPlus = np.linalg.norm(dictionnaryFlattenedBlocsImage[indexBloc]-gravityCenterBlocPlus) 
				distEpsilonMoins = np.linalg.norm(dictionnaryFlattenedBlocsImage[indexBloc]-gravityCenterBlocMoins)
				if distEpsilonPlus > distEpsilonMoins:
					dictionnaryPrototype["Prototype0"][1].append(indexBloc)
				else:
					dictionnaryPrototype["Prototype1"][1].append(indexBloc)
		dictionnaryPrototype = calculGravityCenterBloc(dictionnaryPrototype)
	else :
		print("La fonction : createDictionnaryPrototype() ne gère pas ce format de dictionnaire en entrée.")
		print("Echec du processus !")

	
	return dictionnaryPrototype



# def majDictionnaryPrototype(dictionnaryPrototype):
# 	dictionnaryPrototypeNextIteration = dict()
# 	for key, value in dictionnaryPrototype.items():
		


# 	return None



def lbg(dictionnaryFlattenedBlocsImage):
	dictionnaryPrototype = createDictionnaryPrototype(dictionnaryFlattenedBlocsImage)


	return None