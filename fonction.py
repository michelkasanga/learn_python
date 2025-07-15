def afficheNom(nom, prenom):
    # Fonction pour afficher le nom et le prénom
    print(f'Nom: {nom}, Prénom: {prenom}')

def calcul_somme(a, b):
    # Fonction pour calculer la somme de deux nombres
    return int(a) + int(b)


while True:# boucle infinie jusqu'à ce que l'utilisateur entre des valeurs valides
    try:
        a = int(input('entrez le premier nombre\t'))
        b = int(input('enrez le deuxieume nombre\t'))
        break
    except ValueError:
        print("Veuillez entrer des nombres valides.")

print(calcul_somme(a, b))