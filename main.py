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
    
#----7------ : suppression l'index numero 2:
print('7: suppression index numero 2 :')
del liste_elmnt[2]
for i in liste_elmnt:
    print(i)


#----8---------------------------- : ordonner la  liste:
print('8: voici la liste ordonnée :')
liste_elmnt.sort()
for i in liste_elmnt:
    print(i)
    
#----9----afficher le sens inverse la liste------------:
print("9: voici la liste inverse par rapport oau precedent resultat :")
liste_elmnt.reverse()
for i in liste_elmnt:
    print(i)
    
#----10----vider la liste------------------------------- :
print("10: voici la liste vide :")
liste_elmnt.clear()
print(liste_elmnt)


#----11----supprimer la liste------------------------------- :
print ('11: voici la suppresion de la liste :')
del liste_elmnt
print('liste supprimée avec succes')


# ----------------QUESTION II----------------------------------------------

#----1----afficher le nombre de fois le chiffre 3 apparait_t_il------------------------------- :
tupl = (1,2,3,3,4,5,3,7,8,9)
nbre_fois_3 = 0
check_3 =tupl[0]
print('voici mon tuplet :',tupl)
for i in range(len(tupl)):
    chiffre_3 =tupl[i]
    if chiffre_3 == 3:
        nbre_fois_3 +=1
print("voici le nombre de fois qu'apparait le chiffre 3 :",nbre_fois_3,"fois")

#----2----afficher le contenu de l'element numero 5------------------------------- :

print("voici l'element ",tupl[5])

#----3----ordonner la tuple------------------------------- :

ordonn = sorted(tupl)
print('voici le tuplet ordonné :', ordonn)


#----4----Ajouter un element a la fin de la ligne ------------------------ :

print("voici l'element ajouter a la fin du tuplet :")
tupl = tupl + (4,)
print(tupl)
 
#----5----Ajouter un element a l'index 3 ------------------------ :

print('voici la liste apres ajout d_un element a l_index numero 3:')
tupl = tupl[:3] +(50,)

#----6----affiche la nouvelle tuplet apres l'ajput ------------------------ :
print(tupl)

# ----------------QUESTION III----------------------

st = {'chemise','robe','culotte','wax','maillot','blancket','pantalo','cravate','costume','foullard'}

# ----1---afficher  un  set :

print("voici la liste de mon set :")
for i in st :
    print(i)

# ----2---ajouter un element :

st.add('chaussure')
print("voici la liste de mon set apres avoir ajouter un element:")
for i in st :
    print(i)

#----3---supprimer un element :

st.remove("costume")
print("voici la liste de mon set apres avoir supprimer un element:")
for i in st :
    print(i)

#---4---supprimer un set :

print('voici le set supprimer :')
while st:
    st.discard(max(st))
print(st)


# ----------------QUESTION IV-------------------------------------

Dictionnaire = {'nom':'nday',
                'prenom':'ala',
                'adresse':'carama',
                'email':'ala@gamail.com',
                'telephone':'122333',
                'taille':'1.89cm',
                'profession ':'etudiant',
                'nom_universite':'ULT',
                'Faculte':'info',
                'Departement':'GL'}

# -------1-- affichage d'un dictionnaire:
print("-------1-- affichage d'un dictionnaire")
for i in Dictionnaire.items():
    print(i)