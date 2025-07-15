
capacite_max = 10
capacite_act = 0
no = None
while capacite_act < capacite_max: 
    capacite_act +=1
    print(capacite_act)

#  BREAK
x = 0
while x != 5: #tant que X n'est pas egale à 5 la boucle continuera toujours a tourner
   x+= 2 #on ajoute a chaque fois la boucle tourne
   print(x) #on affiche les nombre genere a chque fois la boucle tourne
   if x == 2000 : #si la boucle atteint le nombre 200000 elle s'arrete de tourneer
       break
print("FIN")

#CONTINUE
liste = [1,2,3,4,5,6]
for element in liste:
    if element == 3:#si les element vaut 3, on passe a l'iteration suivante
        continue
    print(element)