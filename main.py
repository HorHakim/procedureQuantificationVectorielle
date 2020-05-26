#include:utf-8
"""
Author : Cécilia Hakim Zacharie

"""
from generatorDictionnary import *
from Algorithme import *
### Variable du programme 
pathImage = "cartman.png"
tailleBloc = 16


image, numberOfLines, numberOfColones = loadImage(pathImage, tailleBloc)
cv2.imshow('myImage', image)
cv2.waitKey(0)

dictionnaryOfprototypes = imageToDictionnaryOfprototype(pathImage, tailleBloc)
print(dictionnaryOfprototypes["38,42"][255])

gravityCenterBloc = calculGravityCenterBloc(dictionnaryOfprototypes, tailleBloc, numberOfLines, numberOfColones)
print(gravityCenterBloc)
