#include:utf-8
"""
Author : Cécilia Hakim Zacharie 

"""

import cv2
import numpy as np

### Fonctions utiles ###

def loadImage(pathImage, tailleBloc):
	"""Cette fonction load une image correctement(ie on la redimensionne pour que sa taille soit conforme
		à celle des bloc)
		Elle renvoie aussi le nombre de ligne et de colones de l'image"""
	imageLoaded = cv2.imread(pathImage)
	if imageLoaded.shape[0] % tailleBloc  < tailleBloc/2 :
		numberOfLines = imageLoaded.shape[0] - (imageLoaded.shape[0] % tailleBloc )
	else :
		numberOfLines = imageLoaded.shape[0]  - (imageLoaded.shape[0] % tailleBloc) + tailleBloc
	if imageLoaded.shape[1] % tailleBloc  < tailleBloc/2 :
		numberOfColones = imageLoaded.shape[1] - (imageLoaded.shape[1] % tailleBloc )
	else :
		numberOfColones= imageLoaded.shape[1]  - (imageLoaded.shape[1] % tailleBloc) + tailleBloc
	image = cv2.resize(imageLoaded,(numberOfColones, numberOfLines))
	return image, numberOfLines, numberOfColones


def blocToFlattenedBloc(bloc):
	"""Prend en entrée un bloc et renvoie un bloc applati"""
	tailleBloc = len(bloc)
	flattenedBloc = []
	for i in range(tailleBloc):
		for j in range(tailleBloc):
			flattenedBloc.append(bloc[i][j])
	return flattenedBloc


def imageToDictionnaryOfprototype(pathImage, tailleBloc):
	"""
	->	Elle divise une image en bloc, applatit les blocs, les stocque dans un dictionnaire qu'elle renvoit. 
		Les blocs applatits sont indexés dans le dictionnaire en fonction de leur position.
	"""
	dictionnaryOfprototypes = dict()
	image, numberOfLines, numberOfColones = loadImage(pathImage, tailleBloc)
	for i in range(0, numberOfLines, tailleBloc):
		for j in range(0, numberOfColones, tailleBloc):
				indexOfBloc = str(int(i/tailleBloc)) + "," +  str(int(j/tailleBloc))
				bloc = image[i : i + tailleBloc, j : j + tailleBloc]
				flattenedBloc = blocToFlattenedBloc(bloc)
				dictionnaryOfprototypes[indexOfBloc] = flattenedBloc
	return dictionnaryOfprototypes

