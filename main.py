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
    

#----3------ : remplir la 2eme liste avec  les elements de la 1ere liste contenant la lettre 'a' :

print ('3: voici les elements de la nouvelle liste :')


liste_2 = []
for elt in liste_elmnt:
   if 'a' in elt:
       liste_2.append(elt)
for i in liste_2:
    print(i)
    
#----4------ : ajout d'un element a la fin d'une liste:
print('4: ajout_element a la fin :')
liste_elmnt.insert(11,'lion') 
for i in liste_elmnt:
    print(i)
    

#----5------ : ajout d'un element a l'index numero2:
print('5: ajout_element a index numero 2: ')
liste_elmnt.insert(2,'jaguar')
for j in liste_elmnt:
    print(j)
    

#----6------ : suppression d'un element numero 3:
print('6: suppression element numero 3 :')
del liste_elmnt[3]
for i in liste_elmnt:
    print(i)
