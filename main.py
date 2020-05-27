#include:utf-8
"""
Author : Cécilia Hakim Zacharie

"""
from generatorDictionnary import *
from Algorithme import *
### Variable du programme 
pathImage = "cartman.png"
tailleBloc = 16
rgb = True


dictionnaryOfprototypes = imageToDictionnaryOfprototype(pathImage, tailleBloc)
image = dictionnaryOfprototypeToImage(dictionnaryOfprototypes, tailleBloc)
#print(dictionnaryOfprototypes["metaData"])




cv2.imshow('Image Recontruite a partir du dictionnaire de prototypes', image)
cv2.waitKey(0)
