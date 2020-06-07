#include:utf-8
"""
Author : Horairy Hakim

"""
from generatorDictionnary import *
import pickle

def convert(pathImage, tailleBloc, rgb=False):
	with open("DictionnairePrototype", 'rb') as fichier:
		mon_depickler = pickle.Unpickler(fichier)
		DictionnairePrototype = mon_depickler.load()

	dictionnaryFlattenedBlocsImage = imageToDictionnaryFlattenedBlocsImage(pathImage, tailleBloc, rgb)
	dictImage = dict()
	dictImage["metaData"] = dictionnaryFlattenedBlocsImage["metaData"]
	for indexbloc, flattenedBloc in dictionnaryFlattenedBlocsImage.items():
		if indexbloc == "metaData":
			pass
		else:
			dictImage[indexbloc] = "0"
			distMin = np.linalg.norm(flattenedBloc-DictionnairePrototype["Prototype0"])
			for numPrototype, prototype in DictionnairePrototype.items():
				if numPrototype == "metaData":
					pass
				else :
					distBlocPrototype = np.linalg.norm(flattenedBloc-prototype)
					if distBlocPrototype < distMin : 
						dictImage[indexbloc] = numPrototype[9:]
						distMin = distBlocPrototype
		with open(pathImage+'Prototype', 'wb') as fichier:
			mon_pickler = pickle.Pickler(fichier)
			mon_pickler.dump(dictImage)
	return None


def lecture(pathImagePrototype):
	with open("DictionnairePrototype", 'rb') as fichier:
		mon_depickler = pickle.Unpickler(fichier)
		DictionnairePrototype = mon_depickler.load()
	
	with open(pathImagePrototype, 'rb') as fichier:
		mon_depickler = pickle.Unpickler(fichier)
		dictImage  = mon_depickler.load()
	
	for indexbloc, numPrototype in dictImage.items():
		if indexbloc == "metaData":
			pass
		else:
			dictImage[indexbloc] = DictionnairePrototype["Prototype" + str(numPrototype)]
	
	image = dictionnaryFlattenedBlocsImageToImage(dictImage)
	cv2.imshow('Image Recontruite a partir du dictionnaire de prototypes', image)
	cv2.waitKey(0)
	return None










