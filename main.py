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

dictionnaryFlattenedBlocsImage = imageToDictionnaryFlattenedBlocsImage(pathImage, tailleBloc)
image = dictionnaryFlattenedBlocsImageToImage(dictionnaryFlattenedBlocsImage)
#print(dictionnaryFlattenedBlocsImage["metaData"])



#gravityCenterBloc = calculGravityCenterBloc(dictionnaryFlattenedBlocsImage, tailleBloc)
#splitVector(gravityCenterBloc, tailleBloc)
dictionnaryPrototype = createDictionnaryPrototype(dictionnaryFlattenedBlocsImage) # Initialise un dictionnaire de prototype
# print(len(dictionnaryPrototype["gravityCenterBlocPlus"][1]))
# print(len(dictionnaryPrototype["gravityCenterBlocMoins"][1]))
#cv2.imshow('Image Recontruite a partir du dictionnaire de prototypes', image)
#cv2.waitKey(0)
