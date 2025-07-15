contact = {
    'michel':'45286321',
    'ruth': '522666',
    'Euphra': '55555'
}#dictionnaire
for nom, numero in contact.items():
    print(f' {nom} : {numero}')
print('\n')

achat = [1,2,3,5,4,6,9,8,7]#liste
for affichiAchat in achat:
    print(f'numero : {affichiAchat} ')
print('\n')

commande = {1,2,5,8,7,0,0}#tuple
for afficheCommande in commande:
    print(f'commande {afficheCommande}')