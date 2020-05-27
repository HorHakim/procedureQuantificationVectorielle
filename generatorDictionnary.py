#include:utf-8
"""
Author : Cécilia Hakim Zacharie 

"""

import cv2
import math
import numpy as np

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


def imageToDictionnaryOfprototype(pathImage, tailleBloc, rgb=False):
	"""
	->	Elle divise une image en bloc, applatit les blocs, les stocque dans un dictionnaire qu'elle renvoit. 
		Les blocs applatits sont indexés dans le dictionnaire en fonction de leur position.
	"""
	image, numberLinesImage, numberColumnsImage = loadImage(pathImage, tailleBloc, rgb)
	numberBlocs = (int(numberLinesImage/tailleBloc), int(numberColumnsImage/tailleBloc))
	
	dictionnaryOfprototypes = dict()
	dictionnaryOfprototypes["metaData"] = []
	for i in range(0, numberLinesImage - tailleBloc + 1, tailleBloc):
		for j in range(0, numberColumnsImage - tailleBloc + 1, tailleBloc):
				indexBloc = str(int(i/tailleBloc)) + "," +  str(int(j/tailleBloc))
				bloc = image[i : i + tailleBloc, j : j + tailleBloc]
				flattenedBloc = blocToFlattenedBloc(bloc, rgb)
				dictionnaryOfprototypes[indexBloc] = flattenedBloc
				if i == numberLinesImage - tailleBloc and j == numberColumnsImage - tailleBloc :
					dictionnaryOfprototypes["metaData"].append(int(i/tailleBloc)+ 1 )
					dictionnaryOfprototypes["metaData"].append(int(j/tailleBloc)+ 1 )
	
	print("Le dictionnaire de prototype est maintenant construit.")
	
	return dictionnaryOfprototypes


def dictionnaryOfprototypeToImage(dictionnaryOfprototypes, tailleBloc, rgb=False):
	numberLinesBlocs = dictionnaryOfprototypes["metaData"][0]
	numberColumnsBlocs = dictionnaryOfprototypes["metaData"][1]
	numberLinesImage = numberLinesBlocs*tailleBloc
	numberColumnsImage = numberColumnsBlocs*tailleBloc
	
	if rgb:
		image = np.zeros((numberLinesImage, numberColumnsImage, 3), np.uint8)
	else:
		image = np.zeros((numberLinesImage, numberColumnsImage), np.uint8)
	
	for i in range(0, numberLinesImage - tailleBloc + 1, tailleBloc):
		for j in range(0, numberColumnsImage - tailleBloc + 1, tailleBloc):
			indexBloc = str(int(i/tailleBloc)) + "," +  str(int(j/tailleBloc))
			flattenedBloc = dictionnaryOfprototypes[indexBloc]
			bloc = flattenedBlocToBloc(flattenedBloc, rgb)
			image[i : i + tailleBloc, j : j + tailleBloc] = bloc
	
	print("Image reconstruite")
	
	return image


