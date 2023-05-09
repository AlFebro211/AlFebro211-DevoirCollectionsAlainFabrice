# ----------------QUESTION I----------------------

# creation de la liste :

liste_elmnt = ['vache','mouton','chevre','canard','lapin','cochon','abeille','pagna','chat','poule']

#----1------ : affichage des elements de la liste :

print('1: voici la liste des elments de la liste:') 
for element in liste_elmnt:
    print (element)

#----2------ : changer le contenu numero 5 :

print("2: la nouvelle  liste apres le changement  de l'element numero 5:")
liste_elmnt.insert (5,"grenouille")
for element in liste_elmnt:
    print (element)