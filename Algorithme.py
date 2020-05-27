#include:utf-8
"""
Author : Cécilia Hakim Zacharie

"""

import numpy as np

def calculGravityCenterBloc(dictionnaryOfprototypes, tailleBloc):
	"""En cours de construction
		Fonction permettant de calculer le barycentre des blocs du dictionnaryOfPrototyypes"""
	numberLinesBlocs = dictionnaryOfprototypes["metaData"][0]
	numberColumnsBlocs = dictionnaryOfprototypes["metaData"][1]
	numberTotalBlocks = numberLinesBlocs*numberColumnsBlocs
	tailleGravityCenterBloc = tailleBloc**2
	
	gravityCenterBloc = np.zeros((tailleGravityCenterBloc))	
	for i in range(numberLinesBlocs):
		for j in range(numberColumnsBlocs):
			indexBloc = str(int(i/tailleBloc)) + "," +  str(int(j/tailleBloc))
			gravityCenterBloc += dictionnaryOfprototypes[indexBloc]
	
	gravityCenterBloc /= numberTotalBlocks

	return gravityCenterBloc


def splitVector(gravityCenterBloc, tailleBloc):
	epsilonShape = gravityCenterBloc.shape
	epsilon = np.random.random_sample(epsilonShape)
	
	gravityCenterBloc1 = gravityCenterBloc + epsilon
	gravityCenterBloc2 = gravityCenterBloc - epsilon
	
	return gravityCenterBloc1, gravityCenterBloc2