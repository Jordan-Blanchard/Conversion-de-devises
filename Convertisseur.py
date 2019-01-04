import sys

class Conversion():
	def __init__(self, deviseSource, deviseDestination, tauxChange):
		self.deviseSource = deviseSource
		self.deviseDestination = deviseDestination
		self.tauxChange = tauxChange

#Fonction récursive qui sert à déterminer les conversions à faire.
#Deux listes vides appelées conversionsAFaire et conversionsAFaireTempo doivent être instanciées avant d'appeler cette fonction. La liste conversionsAFaire est actualisée après l'exécution de la fonction.
def getConversionsAFaire(listeConversion, deviseSource, deviseDestination):
	global conversionsAFaire
	global conversionsAFaireTempo
	listeConversionTempo=list(listeConversion)

	for conversion in listeConversion:
	
		#On détermine si l'une des devises en cours correspond à celle que l'on cherche
		deviseEnCours=None
		if conversion.deviseSource==deviseSource:
			deviseEnCours=conversion.deviseDestination
		elif conversion.deviseDestination==deviseSource:
			deviseEnCours=conversion.deviseSource
		
		#...Si c'est le cas, on la traite
		if deviseEnCours!=None:
			conversionsAFaireTempo.append(conversion)
		
			#S'il reste des conversionsAFaire à trouver, on appelle récursivement la fonction pour trouver le reste
			if deviseEnCours!=deviseDestination:
				listeConversionTempo.remove(conversion)
				getConversionsAFaire(listeConversionTempo, deviseEnCours, deviseDestination)
				del conversionsAFaireTempo[-1]
			else:
				#Si la liste des conversions à faire est plus courte que la précédente, on l'actualise
				if len(conversionsAFaire)==0 or len(conversionsAFaire)>len(conversionsAFaireTempo):
					conversionsAFaire=list(conversionsAFaireTempo)
				del conversionsAFaireTempo[-1]
				return None

#On ouvre le fichier et on récupère chaque ligne
try:
	with open(sys.argv[1], "r") as fichier:
		lignes=fichier.read().split("\n")
except IOError:
	print ("Le fichier n'a pas pu être ouvert.")
	exit()

#On récupère les premières données
try:
	element=lignes[0].split(";")
	deviseSource=element[0]
	montantSource=element[1]
	deviseDestination=element[2]
except IndexError:
	print("Problème lors de la récupération des données.\nLe fichier est-il correctement formaté ?")
	exit()

#On supprime la première ligne maintenant qu'elle ne nous sert plus
del lignes[0]

#On place les conversions dans une liste de Conversion
listeConversion=[]
for ligne in lignes:
	element=ligne.split(";")
	listeConversion.append(Conversion(element[0], element[1], element[2]))

#On récupère les conversions à faire
conversionsAFaire=[]
conversionsAFaireTempo=[]
getConversionsAFaire(listeConversion, deviseSource, deviseDestination)

if (len(conversionsAFaire)<=0):
	print("La conversion est impossible.")
else:
	#On applique les conversions à faire et on place le résultat dans une variable montantDestination
	deviseEnCours=deviseSource
	montantDestination=float(montantSource)
	for conversionAFaire in conversionsAFaire:
		if conversionAFaire.deviseSource==deviseEnCours:
			deviseEnCours=conversionAFaire.deviseDestination
			montantDestination=montantDestination*float(conversionAFaire.tauxChange)
		elif conversionAFaire.deviseDestination==deviseEnCours:
			deviseEnCours=conversionAFaire.deviseSource
			montantDestination=montantDestination*(1/float(conversionAFaire.tauxChange))

	#On affiche le résultat arrondi à deux chiffres après la virgule
	#Les deux chiffres après la virgule sont conservés même s'il s'agit de zéros
	print (format(round(montantDestination, 2), '.2f'))