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
	print(gravityCenterBloc)
	return gravityCenterBloc

