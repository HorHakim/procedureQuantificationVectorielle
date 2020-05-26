#include:utf-8
"""
Author : Cécilia Hakim Zacharie

"""

import numpy as np

def calculGravityCenterBloc(dictionnaryOfprototypes, tailleBloc, numberOfLines, numberOfColones):
	"""En cours de construction
		Fonction permettant de calculer le barycentre des blocs du dictionnaryOfPrototyypes"""
	dictionnaryOfprototypesLength = len(dictionnaryOfprototypes)
	numberPixelsBloc = (tailleBloc**2)
	numberBlocs = (numberOfLines*numberOfColones)/numberPixelsBloc 
	gravityCenterBloc = numberPixelsBloc*[np.array([ 0,  0, 0])]
	i = 0
	for flattenedBloc in dictionnaryOfprototypes.values():
		for pixel in flattenedBloc :
			gravityCenterBloc[i][0] += (pixel[0]/numberBlocs)
			gravityCenterBloc[i][1] += (pixel[1]/numberBlocs)
			gravityCenterBloc[i][2] += (pixel[2]/numberBlocs)
			i += 1
		i = 0
	return gravityCenterBloc 
