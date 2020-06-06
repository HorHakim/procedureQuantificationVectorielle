#include:utf-8
"""
Author : Cécilia Hakim Zacharie

"""
from generatorDictionnary import *
from Algorithme import *
from Training import *
### Variable du programme 
pathImage = "cartman.png"
tailleBloc = 16
rgb = False


#print(creatorBatch(tailleBloc, rgb=False))
training(tailleBloc, 10)


# dictionnaryFlattenedBlocsImage = imageToDictionnaryFlattenedBlocsImage(pathImage, tailleBloc)
# dictionnaryPrototype = lbg(dictionnaryFlattenedBlocsImage, 15)
# image = lectureDictionnaryPrototype(dictionnaryPrototype)
# cv2.imshow('Image Recontruite a partir du dictionnaire de prototypes', image)
# cv2.waitKey(0)
#image = dictionnaryFlattenedBlocsImageToImage(dictionnaryFlattenedBlocsImage)
#print(dictionnaryFlattenedBlocsImage["metaData"])


#gravityCenterBloc = calculGravityCenterBloc(dictionnaryFlattenedBlocsImage, tailleBloc)
#splitVector(gravityCenterBloc, tailleBloc)
#dictionnaryPrototype = createDictionnaryPrototype(dictionnaryFlattenedBlocsImage) # Initialise un dictionnaire de prototype
#image = lectureDictionnaryPrototype(dictionnaryPrototype)
#print(image)

# print(len(dictionnaryPrototype["gravityCenterBlocPlus"][1]))
# print(len(dictionnaryPrototype["gravityCenterBlocMoins"][1]))

