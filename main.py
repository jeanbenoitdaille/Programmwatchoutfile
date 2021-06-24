import os
import time
     
dossier = "/Users/thibh/Desktop"
dossier_a_chercher = "Python"
     
attente = input("Entrez un temps de rafraichissement: ")
     
while dossier_a_chercher not in os.listdir(dossier):
    	print("Dossier introuvable...")
    	time.sleep(int(attente))
     
print("Trouvé!")