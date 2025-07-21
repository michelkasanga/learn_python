from personnage import Personnage

class Guerrier(Personnage):

    def __init__(self):
        super().__init__()  
        self.force:int = 5

    def attaque(self, cible: Personnage):
        cible.degats(self.force)