# procedureQuantificationVectorielle
Implémentation d'une procédure  de  quantification  vectorielle

Le programme disponible sur ce repertoire permet d'effectuer l'algorithme de Linde–Buzo–Gray (LBG).

Dans le fichier Training.py se trouve la fonction permettant d'implémenter un entrainement(création d'un dictionnaire de prototype) à partir d'une base de donnée.

Dans le fichier generatorDictionnary.py se trouve un ensemble de fonction utile au bon déroulement de l'algorithme.

Dans le fichier Algoritme.py se trouve une fonction nommée lbg() qui permet d'implémenter l'algorithme de Linde–Buzo–Gray au cours de l'entrainement.

Dans le fichier ConvertisseurLecteur.py se trouve les 2 fonctions permettant de convertir une image et de lire une image à l'aide d'un dictionnaire de prototype généré lors d'un entrainement.

Dans le fichier.py 3 fonction peuvent être appellée : 
	- training(tailleBloc, numberIteration) : amorce un entrainement et sauvegarde le dictionnaire de prototype résultant dans un fichier binaire.
	- convert(pathImage, tailleBloc, rgb) : convertit une image à partir d'un dictionnaire de prototype et la sauvegarde en fichier binaire.
	- lecture(pathImagePrototype) pour lire une image (convertie) à partir du dictionnaire de prototype généré lors de l'entrainement.