from personnage import Personnage

class Magicien(Personnage):

    def __init__(self):
        super().__init__()
        self.magie:int = 15

    def lancer_sort(self, cible: Personnage):
        cible.degats(self.magie)