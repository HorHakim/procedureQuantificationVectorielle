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
			if numberTotalBlocs != 0:
				gravityCenterBloc /= numberTotalBlocs
				dictionnary[indexPrototype][0] = gravityCenterBloc
				gravityCenterBloc = np.zeros((tailleGravityCenterBloc))
			else:
				pass	
		 
		dictionnary["metaData"]["UpToDateCentresOfGravity"] == True
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
		dictionnaryPrototype["metaData"]["numberLinesImage"] = dictionnaryFlattenedBlocsImage["metaData"]["numberLinesImage"]
		dictionnaryPrototype["metaData"]["numberColumnsImage"] = dictionnaryFlattenedBlocsImage["metaData"]["numberColumnsImage"]
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





def lbg(dictionnaryFlattenedBlocsImage, numberIteration):
	dictionnaryPrototype = createDictionnaryPrototype(dictionnaryFlattenedBlocsImage)
	tailleBloc = dictionnaryPrototype["metaData"]["tailleBloc"]
	rgb = dictionnaryPrototype["metaData"]["rgb"]

	for iteration in range(numberIteration):
		numberPrototypes = dictionnaryPrototype["metaData"]["numberPrototypes"]
		listGravityCenters = []
		listsIndexBlocs = []
		for k in range(numberPrototypes):
			listIndexBlocsPlus = []
			listIndexBlocsMoins = []
			gravityCenterBlocPlus, gravityCenterBlocMoins = splitVector(dictionnaryPrototype["Prototype" + str(k)][0], tailleBloc)
			listGravityCenters.append(gravityCenterBlocPlus)
			listGravityCenters.append(gravityCenterBlocMoins)
			for indexBloc in dictionnaryPrototype["Prototype" + str(k)][1]:
				distEpsilonPlus = np.linalg.norm(dictionnaryFlattenedBlocsImage[indexBloc]-gravityCenterBlocPlus) 
				distEpsilonMoins = np.linalg.norm(dictionnaryFlattenedBlocsImage[indexBloc]-gravityCenterBlocMoins)
				if distEpsilonPlus > distEpsilonMoins:
					listIndexBlocsMoins.append(indexBloc)
				else:
					listIndexBlocsPlus.append(indexBloc)
			listsIndexBlocs.append(listIndexBlocsPlus)
			listsIndexBlocs.append(listIndexBlocsMoins)
			del dictionnaryPrototype["Prototype" + str(k)]
		for k in range(numberPrototypes*2):
			dictionnaryPrototype["Prototype" + str(k)] = [listGravityCenters[k], listsIndexBlocs[k]]
		dictionnaryPrototype["metaData"]["numberPrototypes"] *= 2
		dictionnaryPrototype["metaData"]["UpToDateCentresOfGravity"] = False
		dictionnaryPrototype = calculGravityCenterBloc(dictionnaryPrototype)

	return dictionnaryPrototype


