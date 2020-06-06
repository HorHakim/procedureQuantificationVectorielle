#include:utf-8
"""
Author : Cécilia Hakim Zacharie 

"""

import cv2
import math
import numpy as np
import os

### Fonctions utiles ###

def loadImage(pathImage, tailleBloc, rgb=False):
	"""Cette fonction load une image correctement(ie on la redimensionne pour que sa taille soit conforme
		à celle des bloc)
		Elle renvoie aussi le nombre de ligne et de colones de l'image"""
	if rgb:
		imageLoaded = cv2.imread(pathImage)
	else: 
		imageLoaded = cv2.imread(pathImage, 0)
	
	print("Chargement de l'image effectué.")
	
	if imageLoaded.shape[0] % tailleBloc  < tailleBloc/2 :
		numberLinesImage = imageLoaded.shape[0] - (imageLoaded.shape[0] % tailleBloc )
	else:
		numberLinesImage = imageLoaded.shape[0]  - (imageLoaded.shape[0] % tailleBloc) + tailleBloc
	
	if imageLoaded.shape[1] % tailleBloc  < tailleBloc/2 :
		numberColumnsImage = imageLoaded.shape[1] - (imageLoaded.shape[1] % tailleBloc )
	else:
		numberColumnsImage= imageLoaded.shape[1]  - (imageLoaded.shape[1] % tailleBloc) + tailleBloc
	
	image = cv2.resize(imageLoaded,(numberColumnsImage, numberLinesImage))
	
	print("L'image est maintenant confome pour être cadrillée.")
	
	return image, numberLinesImage, numberColumnsImage


def blocToFlattenedBloc(bloc,rgb=False):
	"""Prend en entrée un bloc et renvoie un bloc applati"""
	shapeBloc = bloc.shape
	tailleFlattenedBloc = shapeBloc[0]**2
	
	if rgb:
		flattenedBloc = np.zeros((tailleFlattenedBloc,3))
	else:
		flattenedBloc = np.zeros((tailleFlattenedBloc))
	
	for i in range(bloc.shape[0]):
		for j in range(bloc.shape[1]):
			flattenedBloc[i*bloc.shape[0] + j] = bloc[i][j]
	
	return flattenedBloc


def flattenedBlocToBloc(flattenedBloc, rgb=False):
	shapeFlattenedBloc = flattenedBloc.shape
	tailleBloc = int(math.sqrt(shapeFlattenedBloc[0]))
	
	if rgb:
		Bloc = np.zeros((tailleBloc, tailleBloc, 3))
	else:
		Bloc = np.zeros((tailleBloc, tailleBloc))
	
	for i in range(tailleBloc):
		for j in range(tailleBloc):
			Bloc[i][j] = flattenedBloc[i*tailleBloc + j]
	
	return Bloc


def imageToDictionnaryFlattenedBlocsImage(pathImage, tailleBloc, rgb=False):
	"""
	->  Divise une image en bloc, applatit les blocs, les stocke dans un dictionnaire qu'elle renvoit. 
		Les blocs applatits sont indexés dans le dictionnaire en fonction de leur position.
	"""
	image, numberLinesImage, numberColumnsImage = loadImage(pathImage, tailleBloc, rgb)
	numberBlocs = (int(numberLinesImage/tailleBloc), int(numberColumnsImage/tailleBloc))
	
	dictionnaryFlattenedBlocsImage = dict()
	dictionnaryFlattenedBlocsImage["metaData"] = dict()
	dictionnaryFlattenedBlocsImage["metaData"]["typeDictionnary"] = "DictionnaryFlattenedBlocsImage"
	dictionnaryFlattenedBlocsImage["metaData"]["numberLinesImage"] = numberLinesImage
	dictionnaryFlattenedBlocsImage["metaData"]["numberColumnsImage"] = numberColumnsImage 
	dictionnaryFlattenedBlocsImage["metaData"]["numberLinesBlocs"] = int((numberLinesImage - tailleBloc)/tailleBloc)+ 1 
	dictionnaryFlattenedBlocsImage["metaData"]["numberColumnsBlocs"]= int((numberColumnsImage - tailleBloc)/tailleBloc)+ 1 
	dictionnaryFlattenedBlocsImage["metaData"]["tailleBloc"] = tailleBloc
	dictionnaryFlattenedBlocsImage["metaData"]["rgb"] = rgb
	for i in range(0, numberLinesImage - tailleBloc + 1, tailleBloc):
		for j in range(0, numberColumnsImage - tailleBloc + 1, tailleBloc):
				indexBloc = str(int(i/tailleBloc)) + "," +  str(int(j/tailleBloc))
				bloc = image[i : i + tailleBloc, j : j + tailleBloc]
				flattenedBloc = blocToFlattenedBloc(bloc, rgb)
				dictionnaryFlattenedBlocsImage[indexBloc] = flattenedBloc


	
	print("Le dictionnaire de prototype est maintenant construit.")
	
	return dictionnaryFlattenedBlocsImage


def dictionnaryFlattenedBlocsImageToImage(dictionnaryFlattenedBlocsImage):
	
	if dictionnaryFlattenedBlocsImage["metaData"]["typeDictionnary"] == "DictionnaryFlattenedBlocsImage" :
		
		numberLinesBlocs = dictionnaryFlattenedBlocsImage["metaData"]["numberLinesBlocs"]
		numberColumnsBlocs = dictionnaryFlattenedBlocsImage["metaData"]["numberColumnsBlocs"]
		tailleBloc = dictionnaryFlattenedBlocsImage["metaData"]["tailleBloc"]
		rgb = dictionnaryFlattenedBlocsImage["metaData"]["rgb"]
		
		numberLinesImage = numberLinesBlocs*tailleBloc
		numberColumnsImage = numberColumnsBlocs*tailleBloc
		
		if rgb:
			image = np.zeros((numberLinesImage, numberColumnsImage, 3), np.uint8)
		else:
			image = np.zeros((numberLinesImage, numberColumnsImage), np.uint8)
		
		for i in range(0, numberLinesImage - tailleBloc + 1, tailleBloc):
			for j in range(0, numberColumnsImage - tailleBloc + 1, tailleBloc):
				indexBloc = str(int(i/tailleBloc)) + "," +  str(int(j/tailleBloc))
				flattenedBloc = dictionnaryFlattenedBlocsImage[indexBloc]
				bloc = flattenedBlocToBloc(flattenedBloc, rgb)
				image[i : i + tailleBloc, j : j + tailleBloc] = bloc
		
		print("Image reconstruite")
	else :
		image = None
		print("La fonction : dictionnaryFlattenedBlocsImageToImage() ne gère pas ce format de dictionnaire en entrée.")
		print("Echec du processus !")
	
	return image


def creatorBatch(tailleBloc, rgb=False):
	"""renvoie une grande image contenant toutes les images"""
	pathBdd = "./bdd"
	pathsImages = os.listdir(pathBdd)
	for k in range (len(pathsImages)):
		pathsImages[k] = pathBdd + "/" + pathsImages[k]

	batchDictionnaryFlattenedBlocsImage = dict()
	batchDictionnaryFlattenedBlocsImage["metaData"] = dict()
	batchDictionnaryFlattenedBlocsImage["metaData"]["typeDictionnary"] = "DictionnaryFlattenedBlocsImage"
	batchDictionnaryFlattenedBlocsImage["metaData"]["numberLinesImage"] = 0
	batchDictionnaryFlattenedBlocsImage["metaData"]["numberColumnsImage"] = 16
	batchDictionnaryFlattenedBlocsImage["metaData"]["numberLinesBlocs"] = 0
	batchDictionnaryFlattenedBlocsImage["metaData"]["numberColumnsBlocs"]= 1 
	batchDictionnaryFlattenedBlocsImage["metaData"]["tailleBloc"] = tailleBloc
	batchDictionnaryFlattenedBlocsImage["metaData"]["rgb"] = rgb
	compteur = 0
	for pathImage in pathsImages :
		dictionnaryFlattenedBlocsImage = imageToDictionnaryFlattenedBlocsImage(pathImage, tailleBloc, rgb)
		for indexBloc, flattenedBloc in dictionnaryFlattenedBlocsImage.items(): 
			if indexBloc == "metaData":
				pass
			else : 
				indexBlocLine  = int(indexBloc.split(",")[0]) + batchDictionnaryFlattenedBlocsImage["metaData"]["numberLinesBlocs"]
				indexBlocColumn = int(indexBloc.split(",")[1]) + batchDictionnaryFlattenedBlocsImage["metaData"]["numberColumnsBlocs"]
				batchDictionnaryFlattenedBlocsImage[str(compteur) + "," + "0"] = flattenedBloc
				compteur += 1


		batchDictionnaryFlattenedBlocsImage["metaData"]["numberLinesImage"] += dictionnaryFlattenedBlocsImage["metaData"]["numberLinesImage"] * dictionnaryFlattenedBlocsImage["metaData"]["numberColumnsImage"]
		batchDictionnaryFlattenedBlocsImage["metaData"]["numberLinesBlocs"] += dictionnaryFlattenedBlocsImage["metaData"]["numberLinesBlocs"] * dictionnaryFlattenedBlocsImage["metaData"]["numberColumnsBlocs"]

		
	return batchDictionnaryFlattenedBlocsImage


def indexBlocToPostion(indexBloc, tailleBloc):
	L = indexBloc.split(",")
	positionBloc = [int(L[0])*tailleBloc, int(L[1])*tailleBloc]
	return positionBloc


def pasteBlocOnImage(flattenedPrototype, indexBloc, numberLinesImage, numberColumnsImage, tailleBloc, rgb):
	if rgb:
		image = np.zeros((numberLinesImage, numberColumnsImage, 3), np.uint8)
	else:
		image = np.zeros((numberLinesImage, numberColumnsImage), np.uint8)
	bloc = flattenedBlocToBloc(flattenedPrototype)
	i, j = indexBlocToPostion(indexBloc, tailleBloc)
	image[i : i + tailleBloc, j : j + tailleBloc] = bloc
	return image



def lectureDictionnaryPrototype(dictionnaryPrototype):
	numberLinesImage = dictionnaryPrototype["metaData"]["numberLinesImage"]
	numberColumnsImage = dictionnaryPrototype["metaData"]["numberColumnsImage"]
	tailleBloc = dictionnaryPrototype["metaData"]["tailleBloc"]
	rgb = dictionnaryPrototype["metaData"]["rgb"]
	numberLinesBlocs = dictionnaryPrototype["metaData"]["numberLinesBlocs"]
	numberColumnsBlocs = dictionnaryPrototype["metaData"]["numberColumnsBlocs"]
	numberPrototypes = dictionnaryPrototype["metaData"]["numberPrototypes"]
	
	if rgb:
		image = np.zeros((numberLinesImage, numberColumnsImage, 3), np.uint8)
	else:
		image = np.zeros((numberLinesImage, numberColumnsImage), np.uint8)
	for k in range(numberPrototypes):
		flattenedPrototype = np.around(dictionnaryPrototype["Prototype" + str(k)][0])
		flattenedPrototype = flattenedPrototype.astype(int)
		for indexBloc in dictionnaryPrototype["Prototype" + str(k)][1]:
			image += pasteBlocOnImage(flattenedPrototype, indexBloc, numberLinesImage, numberColumnsImage, tailleBloc, rgb)

	return image

