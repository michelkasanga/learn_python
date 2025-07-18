import Billet

def mineur(): #fonction pour l'ecart d'age
   return  range(0, 18)

def majeur(): #fonction pour l'ecart d'age
   return  range(18, 60)

def vieux(): #fonction pour l'ecart d'age
   return  range(60, 100)

def ages(): # Fonction pour demander l'âge
   return  input("Quel est votre age ? ")

def popCorn():
   return  5
            
   

def cinema():
    print("Bienvenue au cinéma !")
    age = int(ages())
    if age in mineur():
        pop = input("voulez vous du pop corn ? ")

        if pop == "oui" or pop == "Oui" or pop == "OUI" or pop == "o" or pop == "O" or pop == "yes" or pop == "Y":
            print(f"Votre billet coûte {Billet.mineur()} euros et votre pop corn {popCorn()} euros.\n Total : {Billet.mineur() + popCorn()} euros.")
        else:
            print(f"Votre billet coûte {Billet.mineur()} euros.")

    elif age in majeur():
        pop = input("voulez vous du pop corn ? ")

        if pop == "oui" or pop == "Oui" or pop == "OUI" or pop == "o" or pop == "O" or pop == "yes" or pop == "Y":
            print(f"Votre billet coûte {Billet.majeur()} euros et votre pop corn {popCorn()} euros.\n Total : {Billet.majeur() + popCorn()} euros.")
        else:
            print(f"Votre billet coûte {Billet.majeur()} euros.")

    elif age in vieux():
        pop = input("voulez vous du pop corn ? ")
        
        if pop == "oui" or pop == "Oui" or pop == "OUI" or pop == "o" or pop == "O" or pop == "yes" or pop == "Y":
            print(f"Votre billet coûte {Billet.vieux()} euros et votre pop corn {popCorn()} euros.\n Total : {Billet.vieux() + popCorn()} euros.")
        else:
            print(f"Votre billet coûte {Billet.vieux()} euros.")
    else:
        print("Vous n'êtes pas autorisé à entrer dans le cinéma.")
        

if __name__ == "__main__":
  while True: # Boucle pour continuer à acheter des billets
    cinema()
    continuer = input("Voulez-vous acheter un autre billet ? (oui/non) ")
    if continuer.lower() != ["oui", "o", "yes", "y"]:
        print("Merci pour l'achat de billet !")
        break
    